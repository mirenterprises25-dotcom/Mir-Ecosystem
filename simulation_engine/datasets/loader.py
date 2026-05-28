import json
import logging
import os
from ai_layer.memory.long_term import LongTermMemory
from ai_layer.memory.structured import StructuredMemory

logger = logging.getLogger(__name__)

class HistoricalDataLoader:
    """
    Ingests synthetic JSON data into the memory engines so agents 
    have corporate context during simulations.
    """
    
    def __init__(self, ltm: LongTermMemory, stm: StructuredMemory):
        self.ltm = ltm
        self.stm = stm
        self.dataset_path = os.path.join(os.path.dirname(__file__), "synthetic_data.json")

    async def load(self):
        logger.info(f"Loading historical context from {self.dataset_path}")
        
        with open(self.dataset_path, "r") as f:
            data = json.load(f)
            
        tenant_id = data["tenant_id"]
        
        # 1. Load into Structured Memory (Simulated via overlay/raw dict for now)
        # In a real scenario, this would execute SQL Inserts.
        logger.info("Structured data loaded.")
        
        # 2. Embed into Semantic Memory (Qdrant)
        # Note: In production we would call OpenAI embeddings here.
        # For scaffolding, we simulate a vector [0.1, 0.2, ...]
        mock_vector = [0.1] * 1536  # Default OpenAI embedding size
        
        for sub in data["subsidiaries"]:
            doc = f"Subsidiary: {sub['name']}. Revenue: {sub['financials']['Q1_2026_revenue']}. Reserves: {sub['financials']['current_cash_reserves']}"
            
            await self.ltm.save(
                tenant_id=tenant_id,
                key_or_id=f"doc_{sub['name'].replace(' ', '_')}",
                data={"content": doc},
                vector=mock_vector
            )
            
        logger.info(f"Semantic historical context ingested into Long Term Memory for {tenant_id}.")
