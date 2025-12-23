#!/usr/bin/env python3
"""
Local ingestion script for textbook content into Qdrant.
This version uses a local file-based Qdrant instance instead of requiring a server.
"""

import json
import tempfile
import os
from qdrant_client import QdrantClient
from qdrant_client.http import models
import uuid
import logging

# Import sentence transformers only conditionally
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LocalRAGService:
    def __init__(self, storage_path=None):
        # Check if SentenceTransformer is available
        if SentenceTransformer is None:
            logger.warning("SentenceTransformer not available, embeddings will not work")
            self.has_embeddings = False
        else:
            self.has_embeddings = True

        # Use provided storage path or create a temporary directory
        if storage_path is None:
            self.storage_path = os.path.join(os.getcwd(), ".qdrant_local")
            os.makedirs(self.storage_path, exist_ok=True)
        else:
            self.storage_path = storage_path

        # Initialize Qdrant client in local mode
        self.client = QdrantClient(path=self.storage_path)

        # Initialize sentence transformer model for embeddings if available
        if self.has_embeddings:
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        else:
            self.embedding_model = None

        # Collection name for textbook content
        self.collection_name = "textbook_content"

        # Initialize the collection if it doesn't exist
        self._initialize_collection()

    def _initialize_collection(self):
        """Initialize the Qdrant collection if it doesn't exist."""
        try:
            collections = self.client.get_collections()
            collection_exists = any(col.name == self.collection_name for col in collections.collections)

            if not collection_exists:
                # Create collection with vector configuration
                # all-MiniLM-L6-v2 outputs 384-dimensional vectors
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
                )
                logger.info(f"Created local Qdrant collection: {self.collection_name}")
            else:
                logger.info(f"Local Qdrant collection {self.collection_name} already exists")

        except Exception as e:
            logger.error(f"Error initializing Qdrant collection: {e}")
            raise

    def _create_embedding(self, text: str) -> list[float]:
        """Create embedding for the given text."""
        if not self.has_embeddings:
            logger.warning("Embeddings not available, returning empty embedding")
            # Return a dummy embedding of appropriate size (384-dim for all-MiniLM-L6-v2)
            return [0.0] * 384

        embedding = self.embedding_model.encode([text])
        return embedding[0].tolist()

    def add_content(self, content_id: str, text: str, metadata: dict = None) -> bool:
        """Add content to the vector store."""
        try:
            # Create embedding for the text
            embedding = self._create_embedding(text)

            # Prepare metadata
            point_metadata = metadata or {}
            point_metadata["content_id"] = content_id
            point_metadata["original_text"] = text

            # Add to Qdrant
            point = models.PointStruct(
                id=content_id,
                vector=embedding,
                payload=point_metadata
            )

            self.client.upsert(
                collection_name=self.collection_name,
                points=[point]
            )

            logger.info(f"Added content to vector store: {content_id}")
            return True

        except Exception as e:
            logger.error(f"Error adding content to vector store: {e}")
            return False

    def add_multiple_content(self, contents: list[dict]) -> bool:
        """Add multiple content items to the vector store."""
        try:
            points = []
            for content in contents:
                content_id = content.get("id", str(uuid.uuid4()))
                text = content.get("text", "")
                metadata = content.get("metadata", {})

                embedding = self._create_embedding(text)

                point_metadata = metadata
                point_metadata["content_id"] = content_id
                point_metadata["original_text"] = text

                point = models.PointStruct(
                    id=content_id,
                    vector=embedding,
                    payload=point_metadata
                )

                points.append(point)

            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )

            logger.info(f"Added {len(contents)} content items to vector store")
            return True

        except Exception as e:
            logger.error(f"Error adding multiple content to vector store: {e}")
            return False

def main():
    logger.info("Starting local textbook ingestion process...")

    # Load the textbook content
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    content_file_path = os.path.join(script_dir, "..", "..", "data", "textbook_content.json")

    if not os.path.exists(content_file_path):
        logger.error(f"Content file not found: {content_file_path}")
        return

    with open(content_file_path, "r") as f:
        contents = json.load(f)

    logger.info(f"Loaded {len(contents)} content items from {content_file_path}")

    # Create local RAG service
    rag_service = LocalRAGService()

    # Add all content to the vector store
    success = rag_service.add_multiple_content(contents)

    if success:
        logger.info(f"Successfully inserted {len(contents)} content items into local Qdrant")
        print(f"✅ Successfully inserted {len(contents)} content items into local Qdrant")
        print(f"💾 Local Qdrant data stored at: {rag_service.storage_path}")
    else:
        logger.error("Failed to insert content into local Qdrant")
        print("❌ Failed to insert content into local Qdrant")

if __name__ == "__main__":
    main()