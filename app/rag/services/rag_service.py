from app.embeddings.models.semantic_search import (
    SemanticSearchRequest
)
from app.embeddings.services.semantic_search_service import (
    SemanticSearchService
)
from app.llm.clients.llm_client import LLMClient
from app.rag.models.rag import (
    RagRequest,
    RagResponse,
    RagSource
)


class RagService:

    def __init__(
        self,
        search_service: SemanticSearchService,
        llm_client: LLMClient
    ) -> None:
        self.search_service = search_service
        self.llm_client = llm_client

    async def ask(
        self,
        request: RagRequest
    ) -> RagResponse:

        # 1. Retrieve relevant chunks
        search_results = await self.search_service.search(
            SemanticSearchRequest(
                query=request.question,
                top_k=request.top_k,
                min_similarity=request.min_similarity
            )
        )

        # 2. Nothing relevant found
        if not search_results:
            return RagResponse(
                answer="I don't know based on the provided context.",
                sources=[]
            )

        # 3. Build context
        context = "\n\n".join(
            f"[Document {result.id}]\n{result.text}"
            for result in search_results
        )

        # 4. Build grounded prompt
        prompt = f"""
Use only the provided context to answer the question.

If the answer cannot be determined from the context,
say: "I don't know based on the provided context."

Context:
{context}

Question:
{request.question}
"""

        # 5. Generate answer
        llm_result = await self.llm_client.generate(
            message=prompt,
            system_prompt=(
                "You are a grounded enterprise knowledge assistant. "
                "Do not invent information that is not present "
                "in the supplied context."
            )
        )

        # 6. Return answer + sources
        return RagResponse(
            answer=llm_result.answer,
            sources=[
                RagSource(
                    id=result.id,
                    text=result.text,
                    similarity=result.similarity
                )
                for result in search_results
            ]
        )