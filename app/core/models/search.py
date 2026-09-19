from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    keyword: str = Field(min_length=1)
    threshold: float = Field(default=0.8, ge=0.0, le=1.0)
    top_k: int = Field(default=2, ge=1, le=100)
