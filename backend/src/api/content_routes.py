from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from ..database.connection import get_db
from ..services.content_service import ContentService

router = APIRouter()
content_service = ContentService()


@router.get("/chapters", response_model=Dict[str, Any])
async def get_all_chapters(db: AsyncSession = Depends(get_db)):
    """
    Retrieve all textbook chapters
    """
    try:
        chapters = await content_service.get_all_chapters(db)
        return {"chapters": chapters}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving chapters: {str(e)}")


@router.get("/chapters/{slug}", response_model=Dict[str, Any])
async def get_chapter_by_slug(slug: str, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a specific textbook chapter by its slug
    """
    try:
        chapter = await content_service.get_chapter_by_slug(db, slug)
        if not chapter:
            raise HTTPException(status_code=404, detail="Chapter not found")
        return chapter
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving chapter: {str(e)}")


@router.get("/chapters/id/{chapter_id}", response_model=Dict[str, Any])
async def get_chapter_by_id(chapter_id: str, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a specific textbook chapter by its ID
    """
    try:
        chapter = await content_service.get_chapter_by_id(db, chapter_id)
        if not chapter:
            raise HTTPException(status_code=404, detail="Chapter not found")
        return chapter
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving chapter: {str(e)}")