from logging import getLogger

from fastapi.exceptions import RequestValidationError
from fastapi import Request, status, FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError


logger = getLogger(__name__)


def init_exception_handlers(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
            request: Request, exc: ValidationError,
    ):
        logger.exception(exc)
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": f"Validation error occurred"
            }
        )
