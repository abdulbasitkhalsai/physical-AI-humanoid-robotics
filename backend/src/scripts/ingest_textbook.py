import json
from services.rag_service import RAGService
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

# Check if RAG is enabled before proceeding
if not settings.rag_enabled:
    logger.info("RAG is disabled via feature flag, skipping textbook ingestion")
    print("RAG is disabled via feature flag, skipping textbook ingestion")
else:
    rag_service = RAGService()

    with open("backend/src/data/textbook_content.json", "r") as f:
        contents = json.load(f)

    success = rag_service.add_multiple_content(contents)
    if success:
        print(f"Inserted {len(contents)} content items into Qdrant")
    else:
        print("Failed to insert content into Qdrant")
