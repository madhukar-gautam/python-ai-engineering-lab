from typing import Protocol


class LLMResult:

    def __init__(
        self,
        answer: str,
        model: str,
        input_tokens: int | None = None,
        output_tokens: int | None = None
    ) -> None:
        self.answer = answer
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens


class LLMClient(Protocol):

    async def generate(
        self,
        message: str,
        system_prompt: str
    ) -> LLMResult:
        ...