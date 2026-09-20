from app.llm.exceptions.llm_error import LLMError


class LLMServiceError(LLMError):
    """Raised when the LLM provider fails."""