from typing import Dict, Any

class MarketSimulation:
    """
    Simulates a sudden market shift (e.g., viral social media trend).
    Primarily designed to test Agent 2 (BI) inventory forecasting and 
    Agent 1 (Financial) cash flow predictions.
    """
    
    @staticmethod
    def generate_parameters(
        product_line: str = "Leather Jackets", 
        demand_spike_percent: int = 300, 
        trigger_source: str = "TikTok Viral Video"
    ) -> Dict[str, Any]:
        
        return {
            "description": f"A {trigger_source} has caused a {demand_spike_percent}% spike in demand for {product_line}.",
            "product_line": product_line,
            "demand_spike_percent": demand_spike_percent,
            "trigger_source": trigger_source,
            "current_inventory": "low",
            "affected_entities": ["MIR Clothing"]
        }
