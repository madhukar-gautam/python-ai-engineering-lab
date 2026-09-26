import re

from app.embeddings.models.semantic_search import (
    SemanticSearchResult
)
from app.rag.vectorstores.vector_store import VectorStore


class KeywordRetriever:

    def __init__(
        self,
        vector_store: VectorStore
    ) -> None:
        self.vector_store = vector_store

    async def retrieve(
        self,
        query: str,
        top_k: int
    ) -> list[SemanticSearchResult]:

        query_terms = self._tokenize(query)

        if not query_terms:
            return []

        results = []

        for document in self.vector_store.get_all():

            document_terms = self._tokenize(
                document.text
            )

            matched_terms = (
                query_terms & document_terms
            )

            if not matched_terms:
                continue

            score = (
                len(matched_terms)
                / len(query_terms)
            )

            results.append(
                SemanticSearchResult(
                    id=document.id,
                    text=document.text,
                    similarity=score
                )
            )

        results.sort(
            key=lambda result: result.similarity,
            reverse=True
        )

        return results[:top_k]

    @staticmethod
    def _tokenize(text: str) -> set[str]:

        return set(
            re.findall(
                r"[a-zA-Z0-9_-]+",
                text.lower()
            )
        )