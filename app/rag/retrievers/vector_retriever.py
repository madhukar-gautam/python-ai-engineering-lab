from app.embeddings.clients.embedding_client import EmbeddingClient
from app.embeddings.models.semantic_search import SemanticSearchResult
from app.rag.vectorstores.vector_store import VectorStore


class VectorRetriever:

    def __init__(
        self,
        embedding_client: EmbeddingClient,
        vector_store: VectorStore
    ) -> None:
        self.embedding_client = embedding_client
        self.vector_store = vector_store

    async def retrieve(
        self,
        query: str,
        top_k: int
    ) -> list[SemanticSearchResult]:

        query_embedding = await self.embedding_client.embed(
            query
        )

        return self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )