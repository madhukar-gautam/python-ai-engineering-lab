from app.llm.clients.openai_client import OpenAIClient
from app.llm.models.chat import ChatRequest, ChatResponse

class ChatService:
    def __init__(self, llm_client: OpenAIClient) -> None:
        self.llm_client = llm_client

    def chat(self, request: ChatRequest) -> ChatResponse:
        answer = self.llm_client.generate(request.message)
        return ChatResponse(answer=answer, model=self.llm_client.model)
