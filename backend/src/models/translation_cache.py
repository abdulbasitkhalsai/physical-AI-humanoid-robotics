from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base
from sqlalchemy.sql import func


class TranslationCache(Base):
    __tablename__ = "translation_cache"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content_id = Column(String, nullable=False, index=True)  # Reference to chapter or content section
    source_language = Column(String, default='en', nullable=False)  # Default: 'en'
    target_language = Column(String, default='ur', nullable=False)  # Default: 'ur'
    source_content_hash = Column(String, nullable=False)  # To detect content changes
    translated_content = Column(Text, nullable=True)  # Cached translation
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)  # Cache expiration