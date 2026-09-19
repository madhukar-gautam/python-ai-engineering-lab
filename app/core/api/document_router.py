from fastapi import APIRouter, Depends

from app.core.models.document import Document
from app.core.models.search import SearchRequest
from app.core.services.document_service import DocumentService
from app.dependencies import get_document_service

router = APIRouter(prefix="/api/v1", tags=["Python Core"])

@router.get("/documents", response_model=list[Document])
def get_documents(
    service: DocumentService = Depends(get_document_service),
) -> list[Document]:
    return service.get_documents()

@router.post("/search", response_model=list[Document])
def search_documents(
    request: SearchRequest,
    service: DocumentService = Depends(get_document_service),
) -> list[Document]:
    return service.search(request)
