from pydantic import BaseModel, Field


class EmbeddingRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=10_000
    )


class EmbeddingResponse(BaseModel):
    dimensions: int
    embedding: list[float]