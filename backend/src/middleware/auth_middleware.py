from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.responses import JSONResponse
from jose import jwt
from fastapi import HTTPException
import os
import logging
from ..services.auth_service import AuthService
from ..database.connection import get_db
from ..models.user import User
import uuid

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Extract token from Authorization header
        auth_header = request.headers.get("authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.replace("Bearer ", "")

            try:
                # Decode the JWT token
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                user_id: str = payload.get("sub")
                token_type: str = payload.get("type")

                if user_id is not None and token_type == "access":
                    # Add user info to request state for use in route handlers
                    user_uuid = uuid.UUID(user_id)
                    request.state.user_id = user_id

                    # Optionally, you could fetch user details here and add to request state
                    # For now, just store the user ID in the request state
                    request.state.user_authenticated = True
                else:
                    request.state.user_authenticated = False
            except jwt.JWTError:
                request.state.user_authenticated = False
        else:
            request.state.user_authenticated = False

        response = await call_next(request)
        return response