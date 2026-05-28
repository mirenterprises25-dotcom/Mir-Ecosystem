import json
import redis.asyncio as redis
from typing import Any, Optional
from ai_layer.memory.base import MemoryLayer
from ai_layer.core.config import settings

class ShortTermMemory(MemoryLayer):
    """
    Operational memory for active tasks and agent scratchpads.
    Backed by Redis. Data is highly ephemeral.
    """
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST, 
            port=settings.REDIS_PORT, 
            decode_responses=True
        )

    def _format_key(self, tenant_id: str, key: str) -> str:
        return f"stm:{tenant_id}:{key}"

    async def save(self, tenant_id: str, key: str, data: Any, ttl: int = 3600) -> bool:
        """Saves data to STM with a default TTL of 1 hour."""
        formatted_key = self._format_key(tenant_id, key)
        await self.client.set(formatted_key, json.dumps(data), ex=ttl)
        return True

    async def retrieve(self, tenant_id: str, key: str, **kwargs) -> Optional[Any]:
        formatted_key = self._format_key(tenant_id, key)
        data = await self.client.get(formatted_key)
        if data:
            return json.loads(data)
        return None

    async def delete(self, tenant_id: str, key: str) -> bool:
        formatted_key = self._format_key(tenant_id, key)
        await self.client.delete(formatted_key)
        return True
