from typing import Protocol

from app.embeddings.models.semantic_search import (
    SemanticSearchResult
)


class Retriever(Protocol):

    async def retrieve(
        self,
        query: str,
        top_k: int
    ) -> list[SemanticSearchResult]:
        ...