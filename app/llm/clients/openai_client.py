import logging
import time

from openai import (
    AsyncOpenAI,
    APITimeoutError,
    APIError
)

from app.config import settings
from app.llm.clients.llm_client import LLMResult
from app.llm.exceptions.llm_service_error import LLMServiceError
from app.llm.exceptions.llm_timeout_error import LLMTimeoutError


logger = logging.getLogger(__name__)


class OpenAIClient:

    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=settings.openai_api_key,
            timeout=settings.llm_timeout_seconds
        )

        self.model = settings.openai_model

    async def generate(
        self,
        message: str,
        system_prompt: str
    ) -> LLMResult:

        start_time = time.perf_counter()

        try:
            response = await self.client.responses.create(
                model=self.model,
                instructions=system_prompt,
                input=message
            )

            usage = response.usage

            return LLMResult(
                answer=response.output_text,
                model=self.model,
                input_tokens=usage.input_tokens if usage else None,
                output_tokens=usage.output_tokens if usage else None
            )

        except APITimeoutError as exc:
            logger.warning(
                "LLM request timed out model=%s",
                self.model
            )

            raise LLMTimeoutError(
                "LLM provider timed out"
            ) from exc

        except APIError as exc:
            logger.exception(
                "LLM provider error model=%s",
                self.model
            )

            raise LLMServiceError(
                "LLM provider request failed"
            ) from exc

        finally:
            latency_ms = (
                time.perf_counter() - start_time
            ) * 1000

            logger.info(
                "LLM request completed model=%s latency_ms=%.2f",
                self.model,
                latency_ms
            )