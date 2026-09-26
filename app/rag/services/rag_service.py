from app.llm.clients.llm_client import LLMClient
from app.rag.models.rag import (
    RagRequest,
    RagResponse,
    RagSource
)
from app.rag.rerankers.reranker import Reranker
from app.rag.retrievers.retriever import Retriever


class RagService:

    def __init__(
        self,
        retriever: Retriever,
        reranker: Reranker,
        llm_client: LLMClient
    ) -> None:
        self.retriever = retriever
        self.reranker = reranker
        self.llm_client = llm_client

    async def ask(
        self,
        request: RagRequest
    ) -> RagResponse:

        # 1. Retrieve relevant chunks
        search_results = await self.retriever.retrieve(
            query=request.question,
            top_k=request.candidate_k
        )

        if not search_results:
            return RagResponse(
                answer="I don't know based on the provided context.",
                sources=[]
            )

        reranked_results = await self.reranker.rerank(
            query=request.question,
            candidates=search_results,
            top_k=request.top_k
        )

        # 3. Build context
        context = "\n\n".join(
            f"[Document {result.id}]\n{result.text}"
            for result in reranked_results
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
                for result in reranked_results
            ]
        )