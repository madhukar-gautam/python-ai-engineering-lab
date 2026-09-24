from app.embeddings.clients.embedding_client import EmbeddingClient
from app.embeddings.models.semantic_search import (
    SemanticSearchRequest,
    SemanticSearchResult
)
from app.rag.vectorstores.vector_store import VectorStore


class SemanticSearchService:

    def __init__(
        self,
        embedding_client: EmbeddingClient,
        vector_store: VectorStore
    ) -> None:

        self.embedding_client = embedding_client
        self.vector_store = vector_store

    async def search(
            self,
            request: SemanticSearchRequest
    ) -> list[SemanticSearchResult]:
        query_embedding = await self.embedding_client.embed(
            request.query
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=request.top_k
        )

        return [
            result
            for result in results
            if result.similarity >= request.min_similarity
        ]