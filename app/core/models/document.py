from pydantic import BaseModel, Field

class Document(BaseModel):
    id: str
    text: str
    score: float = Field(ge=0.0, le=1.0)
