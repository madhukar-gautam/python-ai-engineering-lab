from app.core.repositories.document_repository import DocumentRepository
from app.embeddings.clients.embedding_client import EmbeddingClient
from app.embeddings.models.semantic_search import (
    SemanticSearchRequest,
    SemanticSearchResult
)
from app.embeddings.similarity import cosine_similarity


class SemanticSearchService:

    def __init__(
        self,
        repository: DocumentRepository,
        embedding_client: EmbeddingClient
    ) -> None:
        self.repository = repository
        self.embedding_client = embedding_client

    async def search(
        self,
        request: SemanticSearchRequest
    ) -> list[SemanticSearchResult]:

        # 1. Convert query into vector
        query_embedding = await self.embedding_client.embed(
            request.query
        )

        documents = self.repository.find_all()

        results = []

        # 2. Compare query against every document
        for document in documents:

            document_embedding = await self.embedding_client.embed(
                document.text
            )

            similarity = cosine_similarity(
                query_embedding,
                document_embedding
            )

            results.append(
                SemanticSearchResult(
                    id=document.id,
                    text=document.text,
                    similarity=similarity
                )
            )

        # 3. Highest similarity first
        results.sort(
            key=lambda result: result.similarity,
            reverse=True
        )

        # 4. Return Top-K
        return results[:request.top_k]