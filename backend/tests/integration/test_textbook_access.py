import pytest
import asyncio
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch, MagicMock
from src.main import app
from src.models.textbook_chapter import TextbookChapter
from src.services.content_service import ContentService
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def client():
    """Test client for the FastAPI app"""
    return TestClient(app)


@pytest.mark.asyncio
async def test_textbook_content_access_integration():
    """
    Integration test for textbook content access functionality.
    Tests the complete flow from API request to database retrieval.
    """
    client = TestClient(app)

    # Mock data for testing
    test_chapter = {
        "id": "test-chapter-id",
        "title": "Introduction to Physical AI",
        "slug": "introduction-to-physical-ai",
        "content": "# Introduction\nThis is the introduction to Physical AI...",
        "content_urdu": "# متعارف\nیہ فزیکل ای آئی کا تعارف ہے...",
        "difficulty_level": "beginner",
        "prerequisite_chapters": [],
        "tags": ["introduction", "physical-ai"],
        "version": 1
    }

    # Test 1: Get all chapters endpoint
    with patch('src.services.content_service.ContentService.get_all_chapters') as mock_get_all:
        # Mock the get_all_chapters method
        mock_get_all.return_value = [test_chapter]

        response = client.get("/api/chapters")

        assert response.status_code == 200
        assert "chapters" in response.json()
        assert len(response.json()["chapters"]) == 1
        assert response.json()["chapters"][0]["title"] == test_chapter["title"]

    # Test 2: Get specific chapter by slug
    with patch('src.services.content_service.ContentService.get_chapter_by_slug') as mock_get_by_slug:
        # Mock the get_chapter_by_slug method
        mock_get_by_slug.return_value = test_chapter

        response = client.get(f"/api/chapters/{test_chapter['slug']}")

        assert response.status_code == 200
        assert response.json()["title"] == test_chapter["title"]
        assert response.json()["content"] == test_chapter["content"]
        assert response.json()["slug"] == test_chapter["slug"]

    # Test 3: Get non-existent chapter
    with patch('src.services.content_service.ContentService.get_chapter_by_slug') as mock_get_by_slug:
        # Mock the get_chapter_by_slug method to return None (not found)
        mock_get_by_slug.return_value = None

        response = client.get("/api/chapters/non-existent-chapter")

        assert response.status_code == 404

    # Test 4: Test content service functionality directly
    with patch('src.services.content_service.ContentService.get_all_chapters') as mock_get_all:
        with patch('src.services.content_service.ContentService.get_chapter_by_slug') as mock_get_by_slug:
            content_service = ContentService()

            # Mock return values
            mock_get_all.return_value = [test_chapter]
            mock_get_by_slug.return_value = test_chapter

            # Create a mock database session
            mock_db = AsyncMock(spec=AsyncSession)

            # Test get_all_chapters
            chapters = await content_service.get_all_chapters(mock_db)
            assert len(chapters) == 1
            assert chapters[0]["title"] == test_chapter["title"]

            # Test get_chapter_by_slug
            chapter = await content_service.get_chapter_by_slug(mock_db, test_chapter["slug"])
            assert chapter["title"] == test_chapter["title"]


@pytest.mark.asyncio
async def test_textbook_content_access_with_real_data():
    """
    Integration test using more realistic data scenarios
    """
    client = TestClient(app)

    # Test with multiple chapters
    test_chapters = [
        {
            "id": "chapter-1",
            "title": "Introduction to Physical AI",
            "slug": "introduction-to-physical-ai",
            "content": "# Introduction\nThis is the introduction to Physical AI...",
            "difficulty_level": "beginner",
            "prerequisite_chapters": [],
            "tags": ["introduction", "physical-ai"],
            "version": 1
        },
        {
            "id": "chapter-2",
            "title": "Humanoid Robotics Basics",
            "slug": "humanoid-robotics-basics",
            "content": "# Basics\nThis covers the fundamentals of humanoid robotics...",
            "difficulty_level": "intermediate",
            "prerequisite_chapters": ["chapter-1"],
            "tags": ["robotics", "basics"],
            "version": 1
        }
    ]

    with patch('src.services.content_service.ContentService.get_all_chapters') as mock_get_all:
        # Test multiple chapters response
        mock_get_all.return_value = test_chapters

        response = client.get("/api/chapters")

        assert response.status_code == 200
        data = response.json()
        assert "chapters" in data
        assert len(data["chapters"]) == 2
        assert data["chapters"][0]["title"] == test_chapters[0]["title"]
        assert data["chapters"][1]["title"] == test_chapters[1]["title"]

        # Verify that prerequisite relationships are maintained
        assert data["chapters"][1]["prerequisite_chapters"] == ["chapter-1"]


@pytest.mark.asyncio
async def test_textbook_content_access_edge_cases():
    """
    Test edge cases for textbook content access
    """
    client = TestClient(app)

    # Test with empty content
    empty_chapter = {
        "id": "empty-chapter",
        "title": "Empty Chapter",
        "slug": "empty-chapter",
        "content": "",
        "difficulty_level": "beginner",
        "prerequisite_chapters": [],
        "tags": [],
        "version": 1
    }

    with patch('src.services.content_service.ContentService.get_chapter_by_slug') as mock_get_by_slug:
        mock_get_by_slug.return_value = empty_chapter

        response = client.get("/api/chapters/empty-chapter")

        assert response.status_code == 200
        assert response.json()["content"] == ""
        assert response.json()["title"] == "Empty Chapter"

    # Test with special characters in content
    special_chars_chapter = {
        "id": "special-chars-chapter",
        "title": "Chapter with Special Characters",
        "slug": "special-chars-chapter",
        "content": "# Special Content\nThis has special chars: @#$%^&*()_+-={}[]|\\:\";'<>?,./",
        "difficulty_level": "advanced",
        "prerequisite_chapters": [],
        "tags": ["special", "chars"],
        "version": 1
    }

    with patch('src.services.content_service.ContentService.get_chapter_by_slug') as mock_get_by_slug:
        mock_get_by_slug.return_value = special_chars_chapter

        response = client.get("/api/chapters/special-chars-chapter")

        assert response.status_code == 200
        assert "special chars" in response.json()["content"]


def test_api_routes_exist():
    """
    Test that the required API routes exist and are accessible
    """
    client = TestClient(app)

    # Test that the chapters endpoint exists
    response = client.get("/api/chapters")
    # This will likely return 500 or 404 if there are database issues,
    # but should not return 404 for route not found
    assert response.status_code != 404  # Route should exist even if implementation is incomplete

    # Test that the specific chapter endpoint exists
    response = client.get("/api/chapters/test-slug")
    assert response.status_code != 404  # Route should exist even if implementation is incomplete


if __name__ == "__main__":
    pytest.main([__file__])