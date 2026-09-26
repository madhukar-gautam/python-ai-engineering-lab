from pydantic import BaseModel, Field


class RagRequest(BaseModel):

    question: str = Field(
        min_length=1,
        max_length=10_000
    )

    candidate_k: int = Field(
        default=10,
        ge=1,
        le=50
    )

    top_k: int = Field(
        default=3,
        ge=1,
        le=10
    )

    min_similarity: float = Field(
        default=0.25,
        ge=-1.0,
        le=1.0
    )

class RagSource(BaseModel):
    id: str
    text: str
    similarity: float


class RagResponse(BaseModel):
    answer: str
    sources: list[RagSource]