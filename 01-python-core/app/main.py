from fastapi import FastAPI

from app.api import search_router
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

app.include_router(search_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "UP"
    }