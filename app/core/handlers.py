from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    SkillMatchException,
)


async def skillmatch_exception_handler(
    request: Request,
    exc: Exception,
):
    message = (
        exc.message
        if isinstance(
            exc,
            SkillMatchException,
        )
        else str(exc)
    )

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": message,
        },
    )