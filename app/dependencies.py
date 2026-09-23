from fastapi import Depends

from app.core.repositories.document_repository import DocumentRepository
from app.core.services.document_service import DocumentService
from app.llm.clients.llm_client import LLMClient
from app.llm.clients.openai_client import OpenAIClient
from app.llm.services.chat_service import ChatService
from app.embeddings.clients.embedding_client import EmbeddingClient
from app.embeddings.clients.openai_embedding_client import (
    OpenAIEmbeddingClient
)
from app.embeddings.services.embedding_service import EmbeddingService
from app.embeddings.services.semantic_search_service import (
    SemanticSearchService
)


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
def get_embedding_client() -> EmbeddingClient:
    return OpenAIEmbeddingClient()


def get_embedding_service(
    embedding_client: EmbeddingClient = Depends(
        get_embedding_client
    )
) -> EmbeddingService:

    return EmbeddingService(
        embedding_client
    )
def get_semantic_search_service(
    repository: DocumentRepository = Depends(
        get_document_repository
    ),
    embedding_client: EmbeddingClient = Depends(
        get_embedding_client
    )
) -> SemanticSearchService:

    return SemanticSearchService(
        repository=repository,
        embedding_client=embedding_client
    )