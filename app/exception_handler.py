from fastapi import Request
from fastapi.responses import JSONResponse

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code = 500,
        content = {
            "success": False,
            "message": "Something went wrong. Please try again later.",
        }
    )