from app.evaluation.metrics.retrieval_metrics import (
    precision_at_k,
    recall_at_k,
    reciprocal_rank
)
from app.evaluation.models.evaluation_case import (
    EvaluationCase
)
from app.evaluation.models.evaluation_result import (
    RetrievalCaseResult,
    RetrievalEvaluationResult
)
from app.rag.retrievers.retriever import Retriever


class RetrievalEvaluator:

    def __init__(
        self,
        retriever: Retriever
    ) -> None:
        self.retriever = retriever

    async def evaluate(
        self,
        dataset: list[EvaluationCase],
        k: int,
        retriever_name: str
    ) -> RetrievalEvaluationResult:

        case_results: list[
            RetrievalCaseResult
        ] = []

        for case in dataset:

            retrieved = await self.retriever.retrieve(
                query=case.question,
                top_k=k
            )

            retrieved_ids = [
                result.id
                for result in retrieved
            ]

            recall = recall_at_k(
                retrieved_ids=retrieved_ids,
                relevant_ids=case.expected_source_ids,
                k=k
            )

            precision = precision_at_k(
                retrieved_ids=retrieved_ids,
                relevant_ids=case.expected_source_ids,
                k=k
            )

            rr = reciprocal_rank(
                retrieved_ids=retrieved_ids,
                relevant_ids=case.expected_source_ids
            )

            case_results.append(
                RetrievalCaseResult(
                    case_id=case.id,
                    question=case.question,
                    expected_source_ids=(
                        case.expected_source_ids
                    ),
                    retrieved_source_ids=(
                        retrieved_ids
                    ),
                    recall_at_k=recall,
                    precision_at_k=precision,
                    reciprocal_rank=rr
                )
            )

        total_cases = len(case_results)

        if total_cases == 0:
            return RetrievalEvaluationResult(
                retriever=retriever_name,
                k=k,
                average_recall_at_k=0.0,
                average_precision_at_k=0.0,
                mean_reciprocal_rank=0.0,
                cases=[]
            )

        return RetrievalEvaluationResult(
            retriever=retriever_name,
            k=k,
            average_recall_at_k=sum(
                result.recall_at_k
                for result in case_results
            ) / total_cases,
            average_precision_at_k=sum(
                result.precision_at_k
                for result in case_results
            ) / total_cases,
            mean_reciprocal_rank=sum(
                result.reciprocal_rank
                for result in case_results
            ) / total_cases,
            cases=case_results
        )