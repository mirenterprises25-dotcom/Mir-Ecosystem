from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class MemoryLayer(ABC):
    """
    Abstract base class for all cognitive memory layers.
    """

    @abstractmethod
    async def save(self, tenant_id: str, key_or_id: str, data: Any) -> bool:
        """Saves data into the memory layer, strictly partitioned by tenant."""
        pass

    @abstractmethod
    async def retrieve(self, tenant_id: str, key_or_query: str, **kwargs) -> Optional[Any]:
        """Retrieves data from the memory layer, strictly partitioned by tenant."""
        pass

    @abstractmethod
    async def delete(self, tenant_id: str, key_or_id: str) -> bool:
        """Deletes data from the memory layer."""
        pass
