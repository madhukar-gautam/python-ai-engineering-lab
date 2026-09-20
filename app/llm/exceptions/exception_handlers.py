from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.llm.exceptions.llm_service_error import LLMServiceError
from app.llm.exceptions.llm_timeout_error import LLMTimeoutError


def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(LLMTimeoutError)
    async def handle_llm_timeout(
        request: Request,
        exc: LLMTimeoutError
    ) -> JSONResponse:

        return JSONResponse(
            status_code=504,
            content={
                "error": "LLM_TIMEOUT",
                "message": str(exc)
            }
        )

    @app.exception_handler(LLMServiceError)
    async def handle_llm_service_error(
        request: Request,
        exc: LLMServiceError
    ) -> JSONResponse:

        return JSONResponse(
            status_code=503,
            content={
                "error": "LLM_SERVICE_UNAVAILABLE",
                "message": str(exc)
            }
        )