from typing import Any, Optional, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from ai_layer.memory.base import MemoryLayer

class StructuredMemory(MemoryLayer):
    """
    Ground truth relational memory.
    Reads/writes to the PostgreSQL database.
    Agents should mostly use this for READING factual data (e.g. inventory levels).
    Writes should ideally be routed through API Gateway or careful Orchestrator actions.
    """
    
    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    async def save(self, tenant_id: str, key_or_id: str, data: Dict[str, Any]) -> bool:
        """
        Generic save function. In reality, agents will call specific ORM methods.
        """
        # Scaffold logic: Agents shouldn't arbitrarily write to SQL without schemas.
        # This will be replaced by specific ORM inserts in Phase 4.
        raise NotImplementedError("Direct arbitrary writes to Structured Memory are not allowed. Use specific ORM methods.")

    async def retrieve(self, tenant_id: str, query: str, **kwargs) -> Optional[Any]:
        """
        Executes a controlled read query.
        WARNING: In production, NEVER execute raw SQL from an LLM. 
        This must be parameterized or restricted to specific views.
        """
        # Very basic stub for scaffolding
        result = await self.db.execute(
            text("SELECT 1 as system_online") 
        )
        return result.mappings().all()

    async def delete(self, tenant_id: str, key_or_id: str) -> bool:
        raise NotImplementedError("Agents cannot arbitrarily delete relational data.")
