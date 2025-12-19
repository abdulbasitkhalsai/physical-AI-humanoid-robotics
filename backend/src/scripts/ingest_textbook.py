import json
from services.rag_service import RAGService

rag_service = RAGService()

with open("backend/src/data/textbook_content.json", "r") as f:
    contents = json.load(f)

rag_service.add_multiple_content(contents)
print(f"Inserted {len(contents)} content items into Qdrant")
