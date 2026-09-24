from pydantic import BaseModel


class VectorDocument(BaseModel):
    id: str
    text: str
    embedding: list[float]