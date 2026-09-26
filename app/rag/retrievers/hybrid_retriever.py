from app.embeddings.models.semantic_search import SemanticSearchResult
from app.rag.retrievers.retriever import Retriever


class HybridRetriever:

    def __init__(
        self,
        vector_retriever: Retriever,
        keyword_retriever: Retriever,
        rrf_k: int = 60
    ) -> None:

        self.vector_retriever = vector_retriever
        self.keyword_retriever = keyword_retriever
        self.rrf_k = rrf_k

    async def retrieve(
        self,
        query: str,
        top_k: int
    ) -> list[SemanticSearchResult]:

        vector_results = await self.vector_retriever.retrieve(
            query=query,
            top_k=top_k
        )

        keyword_results = await self.keyword_retriever.retrieve(
            query=query,
            top_k=top_k
        )

        return self._fuse(
            vector_results=vector_results,
            keyword_results=keyword_results,
            top_k=top_k
        )

    def _fuse(
        self,
        vector_results: list[SemanticSearchResult],
        keyword_results: list[SemanticSearchResult],
        top_k: int
    ) -> list[SemanticSearchResult]:

        scores: dict[str, float] = {}
        documents: dict[str, SemanticSearchResult] = {}

        for rank, result in enumerate(
            vector_results,
            start=1
        ):
            scores[result.id] = (
                scores.get(result.id, 0.0)
                + 1.0 / (self.rrf_k + rank)
            )

            documents[result.id] = result

        for rank, result in enumerate(
            keyword_results,
            start=1
        ):
            scores[result.id] = (
                scores.get(result.id, 0.0)
                + 1.0 / (self.rrf_k + rank)
            )

            documents[result.id] = result

        ranked_ids = sorted(
            scores,
            key=scores.get,
            reverse=True
        )

        return [
            SemanticSearchResult(
                id=document_id,
                text=documents[document_id].text,
                similarity=scores[document_id]
            )
            for document_id in ranked_ids[:top_k]
        ]