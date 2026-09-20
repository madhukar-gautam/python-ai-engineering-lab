from fastapi import APIRouter, Depends

from app.dependencies import get_chat_service
from app.llm.models.chat import ChatRequest, ChatResponse
from app.llm.services.chat_service import ChatService

router = APIRouter(prefix="/api/v1/chat", tags=["LLM"])

@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service)
) -> ChatResponse:

    return await service.chat(request)
