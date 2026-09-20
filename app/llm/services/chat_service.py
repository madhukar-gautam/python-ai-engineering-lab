from app.llm.clients.llm_client import LLMClient
from app.llm.models.chat import ChatRequest, ChatResponse


class ChatService:

    def __init__(
        self,
        llm_client: LLMClient
    ) -> None:
        self.llm_client = llm_client

    async def chat(
            self,
            request: ChatRequest
    ) -> ChatResponse:
        result = await self.llm_client.generate(
            message=request.message,
            system_prompt=request.system_prompt
        )

        return ChatResponse(
            answer=result.answer,
            model=result.model,
            input_tokens=result.input_tokens,
            output_tokens=result.output_tokens
        )