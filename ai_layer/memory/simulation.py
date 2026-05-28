from typing import Any, Optional
from ai_layer.memory.base import MemoryLayer
import copy

class SimulationMemory(MemoryLayer):
    """
    Sandboxed wrapper around memory layers.
    Allows agents to "simulate" actions by maintaining a separate, isolated state clone.
    """
    
    def __init__(self, base_memory: MemoryLayer):
        self.base_memory = base_memory
        # In-memory overlay for simulation state
        self._simulation_overlay = {} 

    def _format_sim_key(self, tenant_id: str, key: str) -> str:
        return f"sim:{tenant_id}:{key}"

    async def save(self, tenant_id: str, key_or_id: str, data: Any) -> bool:
        """
        Writes to the simulation overlay, NEVER to the underlying base memory.
        """
        sim_key = self._format_sim_key(tenant_id, key_or_id)
        self._simulation_overlay[sim_key] = copy.deepcopy(data)
        return True

    async def retrieve(self, tenant_id: str, key_or_query: str, **kwargs) -> Optional[Any]:
        """
        First checks the simulation overlay. If not found, reads from the base memory.
        """
        sim_key = self._format_sim_key(tenant_id, key_or_query)
        
        if sim_key in self._simulation_overlay:
            return self._simulation_overlay[sim_key]
            
        # Fallback to read-only access from base memory
        return await self.base_memory.retrieve(tenant_id, key_or_query, **kwargs)

    async def delete(self, tenant_id: str, key_or_id: str) -> bool:
        """
        Marks as deleted in the overlay only.
        """
        sim_key = self._format_sim_key(tenant_id, key_or_id)
        self._simulation_overlay[sim_key] = None # Tombstone
        return True
