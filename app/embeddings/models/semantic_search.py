from pydantic import BaseModel, Field


class SemanticSearchRequest(BaseModel):
    query: str = Field(
        min_length=1,
        max_length=10_000
    )

    top_k: int = Field(
        default=3,
        ge=1,
        le=20
    )


class SemanticSearchResult(BaseModel):
    id: str
    text: str
    similarity: float