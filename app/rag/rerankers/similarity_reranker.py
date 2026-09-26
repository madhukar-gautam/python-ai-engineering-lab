from app.embeddings.models.semantic_search import (
    SemanticSearchResult
)


class SimilarityReranker:

    async def rerank(
        self,
        query: str,
        candidates: list[SemanticSearchResult],
        top_k: int
    ) -> list[SemanticSearchResult]:

        ranked = sorted(
            candidates,
            key=lambda candidate: candidate.similarity,
            reverse=True
        )

        return ranked[:top_k]