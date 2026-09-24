from fastapi import APIRouter, Depends

from app.dependencies import get_rag_service
from app.rag.models.rag import (
    RagRequest,
    RagResponse
)
from app.rag.services.rag_service import RagService
from app.rag.services.ingestion_service import (
    IngestionService
)
from app.dependencies import get_ingestion_service


router = APIRouter(
    prefix="/api/v1/rag",
    tags=["RAG"]
)


@router.post(
    "/ask",
    response_model=RagResponse
)
async def ask(
    request: RagRequest,
    service: RagService = Depends(get_rag_service)
) -> RagResponse:

    return await service.ask(request)
@router.post("/ingest")
async def ingest(
    service: IngestionService = Depends(
        get_ingestion_service
    )
) -> dict[str, int]:

    chunks = await service.ingest()

    return {
        "chunks_indexed": chunks
    }