from fastapi import FastAPI

from app.config import settings
from app.core.api.document_router import router as document_router
from app.llm.api.chat_router import router as chat_router
from app.llm.exceptions.exception_handlers import register_exception_handlers
from app.embeddings.api.embedding_router import (
    router as embedding_router
)
from app.rag.api.rag_router import router as rag_router

import logging
logging.basicConfig(
    level=settings.log_level,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

app = FastAPI(
    title=settings.app_name,
    description="Hands-on lab for Python, LLMs, RAG and Agentic AI",
    version="0.1.0",
)

register_exception_handlers(app)

app.include_router(document_router)
app.include_router(chat_router)

@app.get("/health", tags=["System"])
def health() -> dict[str, str]:
    return {"status": "UP", "environment": settings.environment}
app.include_router(embedding_router)
app.include_router(rag_router)