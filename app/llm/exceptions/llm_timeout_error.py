from app.llm.exceptions.llm_error import LLMError


class LLMTimeoutError(LLMError):
    """Raised when an LLM request times out."""