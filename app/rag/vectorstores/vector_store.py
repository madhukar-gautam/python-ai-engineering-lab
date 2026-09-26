from typing import Protocol

from app.embeddings.models.semantic_search import SemanticSearchResult
from app.rag.models.vector_document import VectorDocument


class VectorStore(Protocol):

    def add(
        self,
        document: VectorDocument
    ) -> None:
        ...

    def search(
        self,
        query_embedding: list[float],
        top_k: int
    ) -> list[SemanticSearchResult]:
        ...

    def get_all(self) -> list[VectorDocument]:
        ...