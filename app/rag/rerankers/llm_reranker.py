import json

from app.embeddings.models.semantic_search import SemanticSearchResult
from app.llm.clients.llm_client import LLMClient


class LLMReranker:

    def __init__(
        self,
        llm_client: LLMClient
    ) -> None:
        self.llm_client = llm_client

    async def rerank(
        self,
        query: str,
        candidates: list[SemanticSearchResult],
        top_k: int
    ) -> list[SemanticSearchResult]:

        if not candidates:
            return []

        candidate_text = "\n\n".join(
            f"ID: {candidate.id}\n"
            f"TEXT: {candidate.text}"
            for candidate in candidates
        )

        prompt = f"""
Question:
{query}

Candidate documents:
{candidate_text}

Select only documents that are genuinely useful for
answering the question.

Return ONLY a JSON array containing document IDs,
ordered from most relevant to least relevant.

Do not include irrelevant documents.

Example:
["2-0", "1-0"]
"""

        result = await self.llm_client.generate(
            message=prompt,
            system_prompt=(
                "You are a document relevance reranker. "
                "Return only valid JSON."
            )
        )

        try:
            selected_ids = json.loads(result.answer)
        except json.JSONDecodeError:
            return candidates[:top_k]

        candidate_map = {
            candidate.id: candidate
            for candidate in candidates
        }

        reranked = [
            candidate_map[document_id]
            for document_id in selected_ids
            if document_id in candidate_map
        ]

        return reranked[:top_k]
