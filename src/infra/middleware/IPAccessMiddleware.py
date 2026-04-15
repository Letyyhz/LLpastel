from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class IPAccessMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, allowed_origins=None):
        super().__init__(app)
        self.allowed_origins = allowed_origins or []

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response