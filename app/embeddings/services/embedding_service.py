from app.embeddings.clients.embedding_client import EmbeddingClient
from app.embeddings.models.embedding import (
    EmbeddingRequest,
    EmbeddingResponse
)


class EmbeddingService:

    def __init__(
        self,
        embedding_client: EmbeddingClient
    ) -> None:
        self.embedding_client = embedding_client

    async def create_embedding(
        self,
        request: EmbeddingRequest
    ) -> EmbeddingResponse:

        vector = await self.embedding_client.embed(
            request.text
        )

        return EmbeddingResponse(
            dimensions=len(vector),
            embedding=vector
        )