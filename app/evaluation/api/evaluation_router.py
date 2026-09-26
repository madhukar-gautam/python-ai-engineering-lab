from fastapi import APIRouter, Depends, Query

from app.dependencies import get_hybrid_retriever
from app.evaluation.datasets.rag_dataset import (
    get_rag_evaluation_dataset
)
from app.evaluation.models.evaluation_result import (
    RetrievalEvaluationResult
)
from app.evaluation.services.retrieval_evaluator import (
    RetrievalEvaluator
)
from app.dependencies import (
    get_vector_retriever,
    get_keyword_retriever,
    get_hybrid_retriever
)

from app.rag.retrievers.vector_retriever import (
    VectorRetriever
)

from app.rag.retrievers.keyword_retriever import (
    KeywordRetriever
)

from app.rag.retrievers.retriever import Retriever


router = APIRouter(
    prefix="/api/v1/evaluation",
    tags=["Evaluation"]
)

async def evaluate_retrieval(
    k: int = Query(default=5, ge=1, le=20),
    retriever: Retriever = Depends(
        get_hybrid_retriever
    )
) -> RetrievalEvaluationResult:

    evaluator = RetrievalEvaluator(
        retriever=retriever
    )

    dataset = get_rag_evaluation_dataset()

    return await evaluator.evaluate(
        dataset=dataset,
        k=k,
        retriever_name="hybrid"
    )
async def run_evaluation(
    retriever: Retriever,
    retriever_name: str,
    k: int
) -> RetrievalEvaluationResult:

    evaluator = RetrievalEvaluator(
        retriever=retriever
    )

    return await evaluator.evaluate(
        dataset=get_rag_evaluation_dataset(),
        k=k,
        retriever_name=retriever_name
    )
@router.post(
    "/retrieval/vector",
    response_model=RetrievalEvaluationResult
)
async def evaluate_vector(
    k: int = Query(default=5, ge=1, le=20),
    retriever: VectorRetriever = Depends(
        get_vector_retriever
    )
) -> RetrievalEvaluationResult:

    return await run_evaluation(
        retriever=retriever,
        retriever_name="vector",
        k=k
    )
@router.post(
    "/retrieval/keyword",
    response_model=RetrievalEvaluationResult
)
async def evaluate_keyword(
    k: int = Query(default=5, ge=1, le=20),
    retriever: KeywordRetriever = Depends(
        get_keyword_retriever
    )
) -> RetrievalEvaluationResult:

    return await run_evaluation(
        retriever=retriever,
        retriever_name="keyword",
        k=k
    )
@router.post(
    "/retrieval/hybrid",
    response_model=RetrievalEvaluationResult
)
async def evaluate_hybrid(
    k: int = Query(default=5, ge=1, le=20),
    retriever: Retriever = Depends(
        get_hybrid_retriever
    )
) -> RetrievalEvaluationResult:

    return await run_evaluation(
        retriever=retriever,
        retriever_name="hybrid",
        k=k
    )