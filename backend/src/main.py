from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .api import content_routes, auth_routes, chatbot_routes, user_routes, translation_routes
from .database.connection import engine
from .utils.logging import setup_logging
from .utils.error_handlers import add_error_handlers
from .middleware.auth_middleware import AuthMiddleware
from .config.settings import settings
import os
import logging

# Setup logging
setup_logging()

app = FastAPI(
    title=settings.app_name,
    description="API for the Physical AI & Humanoid Robotics Textbook platform",
    version=settings.app_version,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
    debug=settings.debug
)

# Add middleware in the appropriate order
app.add_middleware(
    GZipMiddleware,
    minimum_size=1000,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins.split(",") if settings.allowed_origins != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],  # TODO: Use settings for allowed hosts in production
)

app.add_middleware(
    AuthMiddleware,
)

# Include API routes
app.include_router(content_routes.router, prefix=settings.api_prefix, tags=["content"])
app.include_router(auth_routes.router, prefix=f"{settings.api_prefix}/auth", tags=["authentication"])
app.include_router(chatbot_routes.router, prefix=f"{settings.api_prefix}/chatbot", tags=["chatbot"])
app.include_router(user_routes.router, prefix=f"{settings.api_prefix}/users", tags=["users"])
app.include_router(translation_routes.router, prefix=f"{settings.api_prefix}/translate", tags=["translation"])

# Add error handlers
add_error_handlers(app)

@app.on_event("startup")
async def startup_event():
    # Initialize database connection
    logging.info("Application starting up...")
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Cleanup operations
    logging.info("Application shutting down...")
    pass

@app.get("/")
def read_root():
    return {"message": "Physical AI & Humanoid Robotics Textbook API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/health")
def api_health_check():
    return {"status": "healthy", "service": "api"}