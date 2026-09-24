from fastapi import Depends

from app.core.repositories.document_repository import DocumentRepository
from app.core.services.document_service import DocumentService

from app.embeddings.clients.embedding_client import EmbeddingClient
from app.embeddings.clients.openai_embedding_client import OpenAIEmbeddingClient
from app.embeddings.services.embedding_service import EmbeddingService
from app.embeddings.services.semantic_search_service import SemanticSearchService

from app.llm.clients.llm_client import LLMClient
from app.llm.clients.openai_client import OpenAIClient
from app.llm.services.chat_service import ChatService

from app.rag.services.ingestion_service import IngestionService
from app.rag.services.rag_service import RagService
from app.rag.services.text_chunker import TextChunker
from app.rag.vectorstores.in_memory_vector_store import InMemoryVectorStore
from app.rag.vectorstores.vector_store import VectorStore


# =========================================================
# Shared infrastructure
# =========================================================

vector_store = InMemoryVectorStore()


# =========================================================
# Repository dependencies
# =========================================================

def get_document_repository() -> DocumentRepository:
    return DocumentRepository()


# =========================================================
# LLM dependencies
# =========================================================

def get_llm_client() -> LLMClient:
    return OpenAIClient()


# =========================================================
# Embedding dependencies
# =========================================================

def get_embedding_client() -> EmbeddingClient:
    return OpenAIEmbeddingClient()


def get_vector_store() -> VectorStore:
    return vector_store


def get_text_chunker() -> TextChunker:
    return TextChunker(
        chunk_size=50
    )


# =========================================================
# Service dependencies
# =========================================================

def get_document_service(
    repository: DocumentRepository = Depends(
        get_document_repository
    )
) -> DocumentService:

    return DocumentService(repository)


def get_chat_service(
    llm_client: LLMClient = Depends(
        get_llm_client
    )
) -> ChatService:

    return ChatService(llm_client)


def get_embedding_service(
    embedding_client: EmbeddingClient = Depends(
        get_embedding_client
    )
) -> EmbeddingService:

    return EmbeddingService(
        embedding_client
    )


def get_semantic_search_service(
    embedding_client: EmbeddingClient = Depends(
        get_embedding_client
    ),
    vector_store: VectorStore = Depends(
        get_vector_store
    )
) -> SemanticSearchService:

    return SemanticSearchService(
        embedding_client=embedding_client,
        vector_store=vector_store
    )


def get_ingestion_service(
    repository: DocumentRepository = Depends(
        get_document_repository
    ),
    embedding_client: EmbeddingClient = Depends(
        get_embedding_client
    ),
    store: VectorStore = Depends(
        get_vector_store
    ),
    chunker: TextChunker = Depends(
        get_text_chunker
    )
) -> IngestionService:

    return IngestionService(
        repository=repository,
        embedding_client=embedding_client,
        vector_store=store,
        chunker=chunker
    )


def get_rag_service(
    search_service: SemanticSearchService = Depends(
        get_semantic_search_service
    ),
    llm_client: LLMClient = Depends(
        get_llm_client
    )
) -> RagService:

    return RagService(
        search_service=search_service,
        llm_client=llm_client
    )