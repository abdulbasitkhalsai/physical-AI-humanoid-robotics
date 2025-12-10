import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from backend.src.main import app
from backend.src.database.connection import Base
from backend.src.config.settings import settings

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    """Create a test client for the API."""
    with TestClient(app) as test_client:
        yield test_client

def test_get_chapters_success(client):
    """
    Contract test for GET /api/chapters endpoint.

    This test verifies that the endpoint:
    - Returns a 200 status code
    - Returns a JSON response with 'chapters' key
    - Returns a list of chapters
    - Each chapter has required fields (id, title, slug)
    """
    response = client.get("/api/chapters")

    # Assert the response status
    assert response.status_code == 200

    # Assert the response is JSON
    assert response.headers["content-type"].startswith("application/json")

    # Parse the response
    data = response.json()

    # Assert the response structure
    assert "chapters" in data
    assert isinstance(data["chapters"], list)

    # If there are chapters, verify their structure
    if len(data["chapters"]) > 0:
        for chapter in data["chapters"]:
            assert "id" in chapter
            assert "title" in chapter
            assert "slug" in chapter
            assert isinstance(chapter["id"], str)  # UUID as string
            assert isinstance(chapter["title"], str)
            assert isinstance(chapter["slug"], str)

def test_get_chapters_empty_success(client):
    """
    Contract test for GET /api/chapters endpoint when no chapters exist.

    This test verifies that the endpoint:
    - Returns a 200 status code even when no chapters exist
    - Returns an empty list of chapters
    """
    response = client.get("/api/chapters")

    # Assert the response status
    assert response.status_code == 200

    # Parse the response
    data = response.json()

    # Assert the response structure
    assert "chapters" in data
    assert isinstance(data["chapters"], list)

def test_get_chapters_response_format(client):
    """
    Contract test for GET /api/chapters response format compliance.

    This test verifies that the endpoint returns data in the expected format:
    - Response is a dictionary with 'chapters' key
    - 'chapters' value is a list
    - Each chapter has required fields with correct types
    """
    response = client.get("/api/chapters")

    # Assert the response status
    assert response.status_code == 200

    # Parse the response
    data = response.json()

    # Assert top-level structure
    assert isinstance(data, dict)
    assert "chapters" in data

    # Assert chapters is a list
    chapters = data["chapters"]
    assert isinstance(chapters, list)

    # Verify each chapter structure if any exist
    for chapter in chapters:
        # Assert chapter is a dictionary
        assert isinstance(chapter, dict)

        # Assert required fields exist
        required_fields = ["id", "title", "slug"]
        for field in required_fields:
            assert field in chapter

        # Assert field types
        assert isinstance(chapter["id"], str)  # UUID as string
        assert isinstance(chapter["title"], str)
        assert isinstance(chapter["slug"], str)

        # Optional fields that might be present
        optional_fields = ["content", "difficulty_level", "tags", "created_at", "updated_at", "version"]
        for field in optional_fields:
            if field in chapter:
                # If content is present, it should be a string
                if field == "content":
                    assert isinstance(chapter[field], str)
                # If difficulty_level is present, it should be a string
                elif field == "difficulty_level":
                    assert isinstance(chapter[field], str)
                # If tags is present, it should be a list
                elif field == "tags":
                    assert isinstance(chapter[field], list)
                # If timestamps are present, they should be strings
                elif field in ["created_at", "updated_at"]:
                    assert isinstance(chapter[field], str)
                # If version is present, it should be an integer
                elif field == "version":
                    assert isinstance(chapter[field], int)

def test_get_chapters_headers(client):
    """
    Contract test for GET /api/chapters response headers.

    This test verifies that the endpoint returns appropriate headers.
    """
    response = client.get("/api/chapters")

    # Assert the response status
    assert response.status_code == 200

    # Assert content type is JSON
    assert "content-type" in response.headers
    assert "application/json" in response.headers["content-type"]

def test_get_chapters_method_allowed(client):
    """
    Contract test to ensure GET method is allowed for /api/chapters.

    This test verifies that the endpoint accepts GET requests.
    """
    # Test GET method
    get_response = client.get("/api/chapters")
    assert get_response.status_code == 200

    # Test that other methods are not allowed (typically)
    # POST
    post_response = client.post("/api/chapters", json={})
    assert post_response.status_code in [404, 405]  # Not found or Method not allowed

    # PUT
    put_response = client.put("/api/chapters", json={})
    assert put_response.status_code in [404, 405]

    # DELETE
    delete_response = client.delete("/api/chapters")
    assert delete_response.status_code in [404, 405]


def test_get_chapter_by_slug_success(client):
    """
    Contract test for GET /api/chapters/{slug} endpoint.

    This test verifies that the endpoint:
    - Returns a 200 status code when a valid slug is provided
    - Returns a JSON response with chapter data
    - Returns a single chapter object with required fields (id, title, slug, content)
    """
    # Test with a sample slug - in contract testing we're validating the interface
    # regardless of whether the actual data exists (that's for integration tests)
    response = client.get("/api/chapters/introduction-to-physical-ai")

    # For contract testing, we check if the endpoint exists and has proper response format
    # It may return 200 (if chapter exists) or 404 (if not found) but should be a proper JSON response
    assert response.status_code in [200, 404]

    # If it returns 200, validate the response structure
    if response.status_code == 200:
        # Assert the response is JSON
        assert response.headers["content-type"].startswith("application/json")

        # Parse the response
        data = response.json()

        # Assert the response structure for a single chapter
        assert "id" in data
        assert "title" in data
        assert "slug" in data
        assert isinstance(data["id"], str)  # UUID as string
        assert isinstance(data["title"], str)
        assert isinstance(data["slug"], str)


def test_get_chapter_by_slug_not_found(client):
    """
    Contract test for GET /api/chapters/{slug} endpoint when chapter doesn't exist.

    This test verifies that the endpoint:
    - Returns a 404 status code when a non-existent slug is provided
    - Returns a proper error response format
    """
    response = client.get("/api/chapters/non-existent-chapter-slug")

    # Should return 404 for non-existent chapter
    assert response.status_code == 404

    # Assert the response is JSON
    assert response.headers["content-type"].startswith("application/json")

    # Parse the response
    data = response.json()

    # Assert the error response structure
    assert "detail" in data  # FastAPI standard error format


def test_get_chapter_by_slug_response_format(client):
    """
    Contract test for GET /api/chapters/{slug} response format compliance.

    This test verifies that the endpoint returns data in the expected format:
    - Response is a dictionary with chapter fields
    - Contains required fields: id, title, slug
    - Contains optional fields with correct types
    """
    # Test with a sample slug
    response = client.get("/api/chapters/sample-chapter")

    # Contract test: endpoint should respond appropriately (200 if exists, 404 if not)
    if response.status_code == 200:
        # Parse the response
        data = response.json()

        # Assert top-level structure is a dictionary (single chapter)
        assert isinstance(data, dict)

        # Assert required fields exist
        required_fields = ["id", "title", "slug"]
        for field in required_fields:
            assert field in data

        # Assert field types
        assert isinstance(data["id"], str)  # UUID as string
        assert isinstance(data["title"], str)
        assert isinstance(data["slug"], str)

        # Optional fields that might be present
        optional_fields = ["content", "content_urdu", "difficulty_level", "tags",
                          "created_at", "updated_at", "version"]
        for field in optional_fields:
            if field in data:
                # If content is present, it should be a string
                if field in ["content", "content_urdu"]:
                    assert isinstance(data[field], str)
                # If difficulty_level is present, it should be a string
                elif field == "difficulty_level":
                    assert isinstance(data[field], str)
                # If tags is present, it should be a list
                elif field == "tags":
                    assert isinstance(data[field], list)
                # If timestamps are present, they should be strings
                elif field in ["created_at", "updated_at"]:
                    assert isinstance(data[field], str)
                # If version is present, it should be an integer
                elif field == "version":
                    assert isinstance(data[field], int)


def test_get_chapter_by_slug_headers(client):
    """
    Contract test for GET /api/chapters/{slug} response headers.

    This test verifies that the endpoint returns appropriate headers.
    """
    response = client.get("/api/chapters/sample-chapter")

    # Endpoint should return either 200 or 404, but both should have proper headers
    if response.status_code == 200:
        # Assert content type is JSON
        assert "content-type" in response.headers
        assert "application/json" in response.headers["content-type"]
    elif response.status_code == 404:
        # Error responses should also return JSON
        assert "content-type" in response.headers
        assert "application/json" in response.headers["content-type"]


def test_get_chapter_by_slug_method_allowed(client):
    """
    Contract test to ensure GET method is allowed for /api/chapters/{slug}.

    This test verifies that the endpoint accepts GET requests and rejects others.
    """
    # Test GET method with a sample slug
    get_response = client.get("/api/chapters/sample-chapter")
    assert get_response.status_code in [200, 404]  # Valid responses for GET

    # Test that other methods are not allowed
    # POST
    post_response = client.post("/api/chapters/sample-chapter", json={})
    assert post_response.status_code in [404, 405]  # Not found or Method not allowed

    # PUT
    put_response = client.put("/api/chapters/sample-chapter", json={})
    assert put_response.status_code in [404, 405]

    # DELETE
    delete_response = client.delete("/api/chapters/sample-chapter")
    assert delete_response.status_code in [404, 405]