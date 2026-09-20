from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=10_000
    )

    system_prompt: str = Field(
        default="You are a helpful AI engineering assistant.",
        max_length=5_000
    )


class ChatResponse(BaseModel):
    answer: str
    model: str
    input_tokens: int | None = None
    output_tokens: int | None = None