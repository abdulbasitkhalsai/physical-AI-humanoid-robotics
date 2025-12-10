from sqlalchemy import Column, String, DateTime, Text, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base
from sqlalchemy.sql import func
import json


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=True)  # Added from auth implementation
    technical_proficiency = Column(String, nullable=True)  # JSON string for proficiency data
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_activity_at = Column(DateTime(timezone=True), nullable=True)
    data_retention_until = Column(DateTime(timezone=True), nullable=True)

    def set_proficiency(self, proficiency_data):
        """Set technical proficiency as JSON string."""
        self.technical_proficiency = json.dumps(proficiency_data)

    def get_proficiency(self):
        """Get technical proficiency as dict."""
        if self.technical_proficiency:
            return json.loads(self.technical_proficiency)
        return None