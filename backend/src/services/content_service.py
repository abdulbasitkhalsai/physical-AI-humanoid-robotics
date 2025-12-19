from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from ..models.textbook_chapter import TextbookChapter
from ..database.connection import get_db
import logging

logger = logging.getLogger(__name__)


class ContentService:
    def __init__(self):
        pass

    async def get_all_chapters(self, db: AsyncSession) -> List[Dict[str, Any]]:
        """
        Retrieve all textbook chapters from the database
        """
        try:
            result = await db.execute(select(TextbookChapter))
            chapters = result.scalars().all()

            return [
                {
                    "id": str(chapter.id),
                    "title": chapter.title,
                    "slug": chapter.slug,
                    "content": chapter.content,
                    "content_urdu": chapter.content_urdu,
                    "difficulty_level": chapter.difficulty_level,
                    "prerequisite_chapters": chapter.prerequisite_chapters or [],
                    "tags": chapter.tags or [],
                    "version": chapter.version
                }
                for chapter in chapters
            ]
        except Exception as e:
            logger.error(f"Error retrieving all chapters: {e}")
            raise

    async def get_chapter_by_slug(self, db: AsyncSession, slug: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific textbook chapter by its slug
        """
        try:
            result = await db.execute(
                select(TextbookChapter).where(TextbookChapter.slug == slug)
            )
            chapter = result.scalar_one_or_none()

            if chapter:
                return {
                    "id": str(chapter.id),
                    "title": chapter.title,
                    "slug": chapter.slug,
                    "content": chapter.content,
                    "content_urdu": chapter.content_urdu,
                    "difficulty_level": chapter.difficulty_level,
                    "prerequisite_chapters": chapter.prerequisite_chapters or [],
                    "tags": chapter.tags or [],
                    "version": chapter.version
                }
            return None
        except Exception as e:
            logger.error(f"Error retrieving chapter by slug {slug}: {e}")
            raise

    async def get_chapter_by_id(self, db: AsyncSession, chapter_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific textbook chapter by its ID
        """
        try:
            result = await db.execute(
                select(TextbookChapter).where(TextbookChapter.id == chapter_id)
            )
            chapter = result.scalar_one_or_none()

            if chapter:
                return {
                    "id": str(chapter.id),
                    "title": chapter.title,
                    "slug": chapter.slug,
                    "content": chapter.content,
                    "content_urdu": chapter.content_urdu,
                    "difficulty_level": chapter.difficulty_level,
                    "prerequisite_chapters": chapter.prerequisite_chapters or [],
                    "tags": chapter.tags or [],
                    "version": chapter.version
                }
            return None
        except Exception as e:
            logger.error(f"Error retrieving chapter by ID {chapter_id}: {e}")
            raise