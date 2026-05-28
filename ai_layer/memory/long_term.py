from typing import Any, List, Optional
from qdrant_client import AsyncQdrantClient
from qdrant_client.models import PointStruct, Filter, FieldCondition, MatchValue
from ai_layer.memory.base import MemoryLayer
from ai_layer.core.config import settings
import uuid

class LongTermMemory(MemoryLayer):
    """
    Semantic memory for RAG and historical context.
    Backed by Qdrant vector database.
    """
    def __init__(self, collection_name: str = "mir_semantic_memory"):
        self.client = AsyncQdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
        self.collection_name = collection_name

    async def save(self, tenant_id: str, key_or_id: str, data: Any, vector: List[float] = None) -> bool:
        """
        Saves a vector point. 'data' must be a dict containing the payload.
        Requires pre-computed embeddings (vector).
        """
        if not vector:
            raise ValueError("Vector embeddings are required for Long-Term Memory.")
            
        payload = data if isinstance(data, dict) else {"content": str(data)}
        # Strictly inject tenant isolation tag
        payload["tenant_id"] = tenant_id

        point_id = key_or_id if key_or_id else str(uuid.uuid4())
        
        await self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(id=point_id, vector=vector, payload=payload)
            ]
        )
        return True

    async def retrieve(self, tenant_id: str, query_vector: List[float], limit: int = 5, **kwargs) -> Optional[List[Any]]:
        """
        Retrieves semantically similar context, strictly filtered by tenant_id.
        """
        tenant_filter = Filter(
            must=[
                FieldCondition(
                    key="tenant_id",
                    match=MatchValue(value=tenant_id)
                )
            ]
        )
        
        results = await self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            query_filter=tenant_filter,
            limit=limit
        )
        
        return [res.payload for res in results]

    async def delete(self, tenant_id: str, key_or_id: str) -> bool:
        # Simplification for prototype: delete by ID. 
        # In prod, must ensure the point actually belongs to tenant_id before deletion.
        await self.client.delete(
            collection_name=self.collection_name,
            points_selector=[key_or_id]
        )
        return True
