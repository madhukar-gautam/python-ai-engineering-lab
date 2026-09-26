from pydantic import BaseModel, Field


class RetrievalResult(BaseModel):
    id: str
    text: str
    score: float

    retrieval_method: str

    metadata: dict[str, str] = Field(
        default_factory=dict
    )