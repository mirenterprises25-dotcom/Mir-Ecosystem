import logging
from ai_layer.agents.base import BaseAgent
from ai_layer.core.events import BaseEvent, AgentResponseEvent
from ai_layer.llm_router.policies import TaskComplexity

logger = logging.getLogger(__name__)

class FinancialLegalAgent(BaseAgent):
    """
    Agent 1: Handles taxes, S.L. compliance, BOE scraping.
    """
    def __init__(self):
        super().__init__(
            agent_id="Agent-1",
            queue_name="agent1_queue",
            routing_key="task.agent1"
        )

    async def handle_event(self, event: BaseEvent):
        logger.info(f"Agent 1 received subtask: {event.payload}")
        
        tenant_id = event.tenant_id
        action = event.payload.get("action")
        context = event.payload.get("context", {})
        
        result = "Agent 1 Fallback Result"
        
        if action == "analyze_legal":
            # Simulate tools: Here we would fetch vector memory for S.L. regulations
            prompt = f"Analyze the legal and tax implications in Spain for: {context}. Focus on IVA and IRPF."
            result = await self.reason(prompt, complexity=TaskComplexity.HIGH)
            
        # Send response back to Orchestrator
        response_event = AgentResponseEvent(
            tenant_id=tenant_id,
            trace_id=event.trace_id,
            source_agent=self.agent_id,
            status="success",
            payload={"source_agent": self.agent_id, "result": result}
        )
        
        await self.event_bus.publish("task.requested", response_event) # Route back to orchestrator
        await self.log_audit(tenant_id, {"action": action, "result_preview": result[:100]})
