import logging
from typing import Dict, Any
from ai_layer.agents.base import BaseAgent
from ai_layer.core.events import BaseEvent, AgentSubTaskEvent, WorkflowCompletedEvent
from ai_layer.llm_router.policies import TaskComplexity

logger = logging.getLogger(__name__)

class MetaOrchestrator(BaseAgent):
    """
    Agent 3: The Cognitive Governor.
    Receives top-level tasks, breaks them down, delegates, and synthesizes.
    """
    def __init__(self):
        super().__init__(
            agent_id="Agent-3-Orchestrator",
            queue_name="orchestrator_queue",
            routing_key="task.requested"
        )

    async def handle_event(self, event: BaseEvent):
        logger.info(f"Orchestrator received task: {event.event_type}")
        
        if event.event_type == "TaskRequested":
            await self._delegate_sub_tasks(event)
        elif event.event_type == "AgentResponse":
            await self._synthesize_results(event)

    async def _delegate_sub_tasks(self, event: BaseEvent):
        """Breaks down a task and triggers Agent 1 and Agent 2."""
        task_data = event.payload
        tenant_id = event.tenant_id
        
        # In a real scenario, Agent 3 uses LLM here to figure out *who* needs to be called.
        # For scaffolding, we hardcode delegation to both.
        
        # 1. Trigger Agent 1 (Financial/Legal)
        legal_task = AgentSubTaskEvent(
            tenant_id=tenant_id,
            trace_id=event.trace_id,
            target_agent="Agent-1",
            payload={"action": "analyze_legal", "context": task_data}
        )
        await self.event_bus.publish("task.agent1", legal_task)

        # 2. Trigger Agent 2 (Business/Ops)
        biz_task = AgentSubTaskEvent(
            tenant_id=tenant_id,
            trace_id=event.trace_id,
            target_agent="Agent-2",
            payload={"action": "analyze_market", "context": task_data}
        )
        await self.event_bus.publish("task.agent2", biz_task)
        
        # Save state to STM so we know we are waiting for 2 responses
        await self.stm.save(tenant_id, f"workflow:{event.trace_id}:pending", ["Agent-1", "Agent-2"])

    async def _synthesize_results(self, event: BaseEvent):
        """Collects responses from agents and builds the final executive report."""
        tenant_id = event.tenant_id
        trace_id = event.trace_id
        
        # Save this specific agent's response to STM
        await self.stm.save(tenant_id, f"workflow:{trace_id}:resp:{event.payload['source_agent']}", event.payload['result'])
        
        # Check if all pending agents have replied
        pending = await self.stm.retrieve(tenant_id, f"workflow:{trace_id}:pending")
        if pending and event.payload['source_agent'] in pending:
            pending.remove(event.payload['source_agent'])
            await self.stm.save(tenant_id, f"workflow:{trace_id}:pending", pending)
            
            if len(pending) == 0:
                # All agents replied! Synthesize!
                logger.info(f"All agents replied for trace {trace_id}. Synthesizing...")
                
                # Fetch both results from STM
                res1 = await self.stm.retrieve(tenant_id, f"workflow:{trace_id}:resp:Agent-1")
                res2 = await self.stm.retrieve(tenant_id, f"workflow:{trace_id}:resp:Agent-2")
                
                prompt = f"Synthesize these two reports for an Executive Dashboard.\nLegal:\n{res1}\nMarket:\n{res2}"
                final_report = await self.reason(prompt, complexity=TaskComplexity.HIGH)
                
                # Publish completion
                comp_event = WorkflowCompletedEvent(
                    tenant_id=tenant_id,
                    trace_id=trace_id,
                    payload={"executive_summary": final_report}
                )
                await self.event_bus.publish("task.completed", comp_event)
                await self.log_audit(tenant_id, {"action": "synthesized_report", "trace_id": trace_id})
