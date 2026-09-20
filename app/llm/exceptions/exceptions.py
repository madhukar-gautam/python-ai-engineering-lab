class LLMError(Exception):
    """Base exception for LLM-related failures."""


class LLMTimeoutError(LLMError):
    """Raised when the LLM provider exceeds the configured timeout."""


class LLMServiceError(LLMError):
    """Raised when the LLM provider fails."""