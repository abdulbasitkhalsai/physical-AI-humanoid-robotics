from sqlalchemy import Column, String, Text, DateTime, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base
from sqlalchemy.sql import func


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("textbook_chapters.id"), nullable=False, index=True)
    status = Column(String, nullable=True)  # Enum: not_started, in_progress, completed
    completion_percentage = Column(Float, nullable=True)  # 0-100
    time_spent_seconds = Column(Integer, nullable=True)
    last_accessed_at = Column(DateTime(timezone=True), nullable=True)
    notes = Column(Text, nullable=True)  # Optional user notes
    quiz_scores = Column(String, nullable=True)  # JSON string for quiz scores
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Composite unique constraint to ensure one progress record per user-chapter combination
    __table_args__ = (
        # SQLAlchemy doesn't have a direct way to define composite unique constraints
        # This will be handled in the Alembic migration
    )