from fastapi import Depends

from app.core.repositories.document_repository import DocumentRepository
from app.core.services.document_service import DocumentService
from app.llm.clients.llm_client import LLMClient
from app.llm.clients.openai_client import OpenAIClient
from app.llm.services.chat_service import ChatService


def get_document_repository() -> DocumentRepository:
    return DocumentRepository()


def get_document_service(
    repository: DocumentRepository = Depends(
        get_document_repository
    )
) -> DocumentService:

    return DocumentService(repository)


def get_llm_client() -> LLMClient:
    return OpenAIClient()


def get_chat_service(
    llm_client: LLMClient = Depends(get_llm_client)
) -> ChatService:

    return ChatService(llm_client)