from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.dependencies import get_keyword_retriever
from app.embeddings.models.semantic_search import SemanticSearchResult
from app.rag.retrievers.keyword_retriever import KeywordRetriever
from app.rag.retrievers.retriever import Retriever
from app.dependencies import get_hybrid_retriever


router = APIRouter(
    prefix="/api/v1/retrieval",
    tags=["Retrieval"]
)


class KeywordSearchRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)


@router.post(
    "/keyword",
    response_model=list[SemanticSearchResult]
)
async def keyword_search(
    request: KeywordSearchRequest,
    retriever: KeywordRetriever = Depends(
        get_keyword_retriever
    )
) -> list[SemanticSearchResult]:

    return await retriever.retrieve(
        query=request.query,
        top_k=request.top_k
    )
@router.post(
    "/hybrid",
    response_model=list[SemanticSearchResult]
)
async def hybrid_search(
    request: KeywordSearchRequest,
    retriever: Retriever = Depends(
        get_hybrid_retriever
    )
) -> list[SemanticSearchResult]:

    return await retriever.retrieve(
        query=request.query,
        top_k=request.top_k
    )