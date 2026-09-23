from fastapi import APIRouter, Depends

from app.dependencies import get_embedding_service
from app.embeddings.models.embedding import (
    EmbeddingRequest,
    EmbeddingResponse
)
from app.embeddings.services.embedding_service import EmbeddingService
from app.embeddings.models.semantic_search import (
    SemanticSearchRequest,
    SemanticSearchResult
)

from app.embeddings.services.semantic_search_service import (
    SemanticSearchService
)

from app.dependencies import get_semantic_search_service


router = APIRouter(
    prefix="/api/v1/embeddings",
    tags=["Embeddings"]
)


@router.post(
    "",
    response_model=EmbeddingResponse
)
async def create_embedding(
    request: EmbeddingRequest,
    service: EmbeddingService = Depends(
        get_embedding_service
    )
) -> EmbeddingResponse:

    return await service.create_embedding(request)

@router.post(
    "/search",
    response_model=list[SemanticSearchResult]
)
async def semantic_search(
    request: SemanticSearchRequest,
    service: SemanticSearchService = Depends(
        get_semantic_search_service
    )
) -> list[SemanticSearchResult]:

    return await service.search(request)