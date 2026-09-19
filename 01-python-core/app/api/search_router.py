from fastapi import APIRouter

from app.models import Document, SearchRequest
from app.repositories import DocumentRepository
from app.services import DocumentService


router = APIRouter(
    prefix="/api/v1",
    tags=["Search"]
)

repository = DocumentRepository()
service = DocumentService(repository)


@router.post(
    "/search",
    response_model=list[Document]
)
def search_documents(
    request: SearchRequest
) -> list[Document]:
    return service.search(request)


@router.get(
    "/documents",
    response_model=list[Document]
)
def get_documents() -> list[Document]:
    return service.get_documents()