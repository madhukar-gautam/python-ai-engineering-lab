from openai import AsyncOpenAI

from app.config import settings


class OpenAIEmbeddingClient:

    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=settings.openai_api_key,
            timeout=settings.llm_timeout_seconds
        )

        self.model = settings.embedding_model

    async def embed(
        self,
        text: str
    ) -> list[float]:

        response = await self.client.embeddings.create(
            model=self.model,
            input=text
        )

        return response.data[0].embedding