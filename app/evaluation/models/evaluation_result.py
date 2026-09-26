from pydantic import BaseModel


class RetrievalCaseResult(BaseModel):
    case_id: str
    question: str

    expected_source_ids: list[str]
    retrieved_source_ids: list[str]

    recall_at_k: float
    precision_at_k: float
    reciprocal_rank: float


class RetrievalEvaluationResult(BaseModel):
    retriever: str
    k: int

    average_recall_at_k: float
    average_precision_at_k: float
    mean_reciprocal_rank: float

    cases: list[RetrievalCaseResult]