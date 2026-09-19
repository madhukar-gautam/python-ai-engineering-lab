from fastapi import FastAPI

from app.config import settings
from app.core.api.document_router import router as document_router
from app.llm.api.chat_router import router as chat_router

app = FastAPI(
    title=settings.app_name,
    description="Hands-on lab for Python, LLMs, RAG and Agentic AI",
    version="0.1.0",
)

app.include_router(document_router)
app.include_router(chat_router)

@app.get("/health", tags=["System"])
def health() -> dict[str, str]:
    return {"status": "UP", "environment": settings.environment}
