from sqlalchemy import Column, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base
from sqlalchemy.sql import func


class ChatbotMessage(Base):
    __tablename__ = "chatbot_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("chatbot_sessions.id"), nullable=False, index=True)
    role = Column(String, nullable=False)  # Enum: user, assistant
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    source_chunks = Column(String, nullable=True)  # JSON string for source chunks
    is_fallback_response = Column(Boolean, default=False)  # True if response was generated due to out-of-scope query