from app.core.repositories.document_repository import (
    DocumentRepository
)
from app.embeddings.clients.embedding_client import (
    EmbeddingClient
)
from app.rag.models.vector_document import VectorDocument
from app.rag.services.text_chunker import TextChunker
from app.rag.vectorstores.vector_store import VectorStore


class IngestionService:

    def __init__(
        self,
        repository: DocumentRepository,
        embedding_client: EmbeddingClient,
        vector_store: VectorStore,
        chunker: TextChunker
    ) -> None:

        self.repository = repository
        self.embedding_client = embedding_client
        self.vector_store = vector_store
        self.chunker = chunker

    async def ingest(self) -> int:

        documents = self.repository.find_all()

        chunk_count = 0

        for document in documents:

            chunks = self.chunker.chunk(
                document.text
            )

            for index, chunk in enumerate(chunks):

                embedding = await self.embedding_client.embed(
                    chunk
                )

                vector_document = VectorDocument(
                    id=f"{document.id}-{index}",
                    text=chunk,
                    embedding=embedding
                )

                self.vector_store.add(
                    vector_document
                )

                chunk_count += 1

        return chunk_count