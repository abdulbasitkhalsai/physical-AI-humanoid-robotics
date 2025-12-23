from pydantic_settings import BaseSettings
from typing import Optional
import os
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    # Application settings
    app_name: str = "Physical AI & Humanoid Robotics Textbook API"
    app_version: str = "1.0.0"
    environment: Environment = Environment.DEVELOPMENT
    debug: bool = False

    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/physical_ai_textbook")
    database_pool_size: int = int(os.getenv("DATABASE_POOL_SIZE", "5"))
    database_pool_timeout: int = int(os.getenv("DATABASE_POOL_TIMEOUT", "30"))

    # Authentication settings
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    refresh_token_expire_days: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

    # Qdrant settings
    qdrant_host: str = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port: int = int(os.getenv("QDRANT_PORT", "6333"))
    qdrant_https: bool = os.getenv("QDRANT_HTTPS", "false").lower() == "true"
    qdrant_api_key: Optional[str] = os.getenv("QDRANT_API_KEY")

    # OpenAI settings
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")

    # CORS settings
    allowed_origins: str = os.getenv("ALLOWED_ORIGINS", "*")

    # Logging settings
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    # API settings
    api_prefix: str = "/api"
    docs_url: str = "/api/docs"
    redoc_url: str = "/api/redoc"

    # File upload settings
    max_upload_size: int = int(os.getenv("MAX_UPLOAD_SIZE", "10485760"))  # 10MB in bytes
    allowed_file_types: str = os.getenv("ALLOWED_FILE_TYPES", "application/pdf,text/plain,text/markdown")

    # RAG settings
    rag_enabled: bool = os.getenv("RAG_ENABLED", "false").lower() == "true"

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create a singleton instance of settings
settings = Settings()