from typing import List, Dict, Optional, Any
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct, VectorParams, Distance
import uuid
from config.settings import settings
import logging

# Import sentence transformers only if RAG is enabled
if settings.rag_enabled:
    from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

class RAGService:
    def __init__(self):
        # Check if RAG is enabled
        if not settings.rag_enabled:
            logger.info("RAG service is disabled via feature flag")
            self.enabled = False
            return

        # Initialize Qdrant client with configuration from settings
        if settings.qdrant_https:
            self.client = QdrantClient(
                url=settings.qdrant_url,
                port=settings.qdrant_port,
                api_key=settings.qdrant_api_key,
                https=True
            )
        else:
            self.client = QdrantClient(
                host=settings.qdrant_host,
                port=settings.qdrant_port,
                api_key=settings.qdrant_api_key
            )

        # Initialize sentence transformer model for embeddings
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

        # Collection name for textbook content
        self.collection_name = "textbook_content"

        # Initialize the collection if it doesn't exist
        self._initialize_collection()

        self.enabled = True

    def _initialize_collection(self):
        """Initialize the Qdrant collection if it doesn't exist."""
        if not settings.rag_enabled:
            logger.info("RAG is disabled, skipping collection initialization")
            return

        try:
            collections = self.client.get_collections()
            collection_exists = any(col.name == self.collection_name for col in collections.collections)

            if not collection_exists:
                # Create collection with vector configuration
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=384, distance=Distance.COSINE),  # all-MiniLM-L6-v2 outputs 384-dim vectors
                )

                logger.info(f"Created Qdrant collection: {self.collection_name}")
            else:
                logger.info(f"Qdrant collection {self.collection_name} already exists")

        except Exception as e:
            logger.error(f"Error initializing Qdrant collection: {e}")
            raise

    def _create_embedding(self, text: str) -> List[float]:
        """Create embedding for the given text."""
        if not settings.rag_enabled:
            logger.warning("RAG is disabled, returning empty embedding")
            # Return a dummy embedding of appropriate size (384-dim for all-MiniLM-L6-v2)
            return [0.0] * 384

        embedding = self.embedding_model.encode([text])
        return embedding[0].tolist()

    def add_content(self, content_id: str, text: str, metadata: Optional[Dict[str, Any]] = None) -> bool:
        """Add content to the vector store."""
        if not settings.rag_enabled:
            logger.info("RAG is disabled, skipping content addition")
            return False

        try:
            # Create embedding for the text
            embedding = self._create_embedding(text)

            # Prepare metadata
            point_metadata = metadata or {}
            point_metadata["content_id"] = content_id
            point_metadata["original_text"] = text

            # Add to Qdrant
            point = PointStruct(
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

    def add_multiple_content(self, contents: List[Dict[str, Any]]) -> bool:
        """Add multiple content items to the vector store."""
        if not settings.rag_enabled:
            logger.info("RAG is disabled, skipping multiple content addition")
            return False

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

                point = PointStruct(
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

    def search_content(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search for content similar to the query."""
        if not settings.rag_enabled:
            logger.info("RAG is disabled, returning empty search results")
            return []

        try:
            # Create embedding for the query
            query_embedding = self._create_embedding(query)

            # Search in Qdrant
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                with_payload=True
            )

            results = []
            for result in search_results:
                results.append({
                    "id": result.id,
                    "score": result.score,
                    "text": result.payload.get("original_text", ""),
                    "metadata": {k: v for k, v in result.payload.items() if k not in ["original_text"]}
                })

            logger.info(f"Search completed with {len(results)} results")
            return results

        except Exception as e:
            logger.error(f"Error searching content: {e}")
            return []

    def delete_content(self, content_id: str) -> bool:
        """Delete content from the vector store by ID."""
        if not settings.rag_enabled:
            logger.info("RAG is disabled, skipping content deletion")
            return False

        try:
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=models.PointIdsList(
                    points=[content_id]
                )
            )

            logger.info(f"Deleted content from vector store: {content_id}")
            return True

        except Exception as e:
            logger.error(f"Error deleting content: {e}")
            return False

    def get_content_by_id(self, content_id: str) -> Optional[Dict[str, Any]]:
        """Get content by ID."""
        if not settings.rag_enabled:
            logger.info("RAG is disabled, returning None for content by ID")
            return None

        try:
            points = self.client.retrieve(
                collection_name=self.collection_name,
                ids=[content_id],
                with_payload=True
            )

            if points and len(points) > 0:
                point = points[0]
                return {
                    "id": point.id,
                    "text": point.payload.get("original_text", ""),
                    "metadata": {k: v for k, v in point.payload.items() if k not in ["original_text"]}
                }

            return None

        except Exception as e:
            logger.error(f"Error getting content by ID: {e}")
            return None

    def clear_collection(self) -> bool:
        """Clear all content from the collection."""
        if not settings.rag_enabled:
            logger.info("RAG is disabled, skipping collection clearing")
            return False

        try:
            # Get all point IDs
            all_points = self.client.scroll(
                collection_name=self.collection_name,
                limit=10000  # Adjust as needed
            )[0]

            if all_points:
                point_ids = [point.id for point in all_points]

                # Delete all points
                self.client.delete(
                    collection_name=self.collection_name,
                    points_selector=models.PointIdsList(
                        points=point_ids
                    )
                )

            logger.info("Cleared collection")
            return True

        except Exception as e:
            logger.error(f"Error clearing collection: {e}")
            return False