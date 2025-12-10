from sqlalchemy import Column, String, Text, DateTime, Integer, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base
from sqlalchemy.sql import func


class TextbookChapter(Base):
    __tablename__ = "textbook_chapters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False, index=True)
    content = Column(Text, nullable=False)  # Markdown format
    content_urdu = Column(Text, nullable=True)  # Translated content in Urdu
    difficulty_level = Column(String, nullable=True)  # Enum: beginner, intermediate, advanced
    prerequisite_chapters = Column(ARRAY(String), nullable=True)  # Array of UUIDs as strings
    tags = Column(ARRAY(String), nullable=True)  # Array of tag strings
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    version = Column(Integer, default=1)