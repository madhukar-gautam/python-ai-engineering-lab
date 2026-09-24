from app.embeddings.models.semantic_search import (
    SemanticSearchResult
)
from app.embeddings.similarity import cosine_similarity
from app.rag.models.vector_document import VectorDocument


class InMemoryVectorStore:

    def __init__(self) -> None:
        self.documents: list[VectorDocument] = []

    def add(
        self,
        document: VectorDocument
    ) -> None:
        self.documents.append(document)

    def search(
        self,
        query_embedding: list[float],
        top_k: int
    ) -> list[SemanticSearchResult]:

        results = []

        for document in self.documents:

            similarity = cosine_similarity(
                query_embedding,
                document.embedding
            )

            results.append(
                SemanticSearchResult(
                    id=document.id,
                    text=document.text,
                    similarity=similarity
                )
            )

        results.sort(
            key=lambda result: result.similarity,
            reverse=True
        )

        return results[:top_k]