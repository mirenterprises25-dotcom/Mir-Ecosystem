import logging
from ai_layer.agents.base import BaseAgent
from ai_layer.core.events import BaseEvent, AgentResponseEvent
from ai_layer.llm_router.policies import TaskComplexity

logger = logging.getLogger(__name__)

class BusinessIntelligenceAgent(BaseAgent):
    """
    Agent 2: Handles market trends, BI, inventory, and marketing.
    """
    def __init__(self):
        super().__init__(
            agent_id="Agent-2",
            queue_name="agent2_queue",
            routing_key="task.agent2"
        )

    async def handle_event(self, event: BaseEvent):
        logger.info(f"Agent 2 received subtask: {event.payload}")
        
        tenant_id = event.tenant_id
        action = event.payload.get("action")
        context = event.payload.get("context", {})
        
        result = "Agent 2 Fallback Result"
        
        if action == "analyze_market":
            # Simulate tools: Here we would fetch competitor pricing & social media sentiment
            prompt = f"Analyze the market trend, predicted demand, and competitor pricing for: {context}."
            result = await self.reason(prompt, complexity=TaskComplexity.MEDIUM)
            
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
