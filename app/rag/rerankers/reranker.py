from typing import Protocol

from app.embeddings.models.semantic_search import (
    SemanticSearchResult
)


class Reranker(Protocol):

    async def rerank(
        self,
        query: str,
        candidates: list[SemanticSearchResult],
        top_k: int
    ) -> list[SemanticSearchResult]:
        ...