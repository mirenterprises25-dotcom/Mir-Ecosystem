import logging
import uuid
from typing import Dict, Any, Type
from ai_layer.core.messaging import EventBus
from ai_layer.core.events import TaskRequestedEvent

logger = logging.getLogger(__name__)

class SimulationEngine:
    """
    Spins up an isolated simulation scenario and triggers the Orchestrator.
    It feeds the Orchestrator a modified context so the agents believe the 
    simulated conditions are real.
    """
    def __init__(self):
        self.event_bus = EventBus()

    async def run_scenario(self, tenant_id: str, scenario_name: str, parameters: Dict[str, Any]):
        """
        Triggers a simulation workflow.
        """
        sim_id = f"sim-{uuid.uuid4()}"
        logger.info(f"Starting simulation {sim_id} for scenario: {scenario_name}")
        
        # In a full implementation, this engine would push the simulated variables
        # into the `SimulationMemory` overlay for the agents to read.
        
        # Build the simulated context to pass to the Orchestrator
        simulated_context = {
            "simulation_id": sim_id,
            "scenario": scenario_name,
            "simulated_variables": parameters,
            "instruction": f"URGENT: This is a simulation. Act as if {scenario_name} just occurred with these parameters: {parameters}. Generate an executive impact report."
        }
        
        # Trigger the Orchestrator via RabbitMQ
        event = TaskRequestedEvent(
            tenant_id=tenant_id,
            trace_id=sim_id, # Use sim_id as trace_id to track the whole simulation flow
            payload=simulated_context
        )
        
        await self.event_bus.connect()
        await self.event_bus.publish("task.requested", event)
        logger.info(f"Simulation {sim_id} dispatched to Orchestrator.")
        return sim_id
