import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from ai_layer.core.messaging import EventBus
from ai_layer.core.events import BaseEvent
from ai_layer.llm_router.router import LLMRouter
from ai_layer.llm_router.policies import TaskComplexity
from ai_layer.memory.short_term import ShortTermMemory
from ai_layer.memory.audit import AuditMemory

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """
    Abstract base class for all MIR-Ecosystem Agents.
    Provides standard tools: Event Bus, LLM Router, and Memory Layers.
    """
    def __init__(self, agent_id: str, queue_name: str, routing_key: str):
        self.agent_id = agent_id
        self.queue_name = queue_name
        self.routing_key = routing_key
        
        self.event_bus = EventBus()
        self.router = LLMRouter()
        self.stm = ShortTermMemory()
        self.audit = AuditMemory()

    async def start(self):
        """Connects to RabbitMQ and starts listening for tasks."""
        await self.event_bus.connect()
        await self.event_bus.subscribe(self.queue_name, self.routing_key, self.handle_event)
        logger.info(f"Agent {self.agent_id} started and listening to {self.queue_name}")

    @abstractmethod
    async def handle_event(self, event: BaseEvent):
        """Must be implemented by specific agents to process incoming tasks."""
        pass

    async def reason(self, prompt: str, complexity: TaskComplexity = TaskComplexity.MEDIUM) -> str:
        """Standard wrapper to call the LLM Router."""
        messages = [{"role": "user", "content": prompt}]
        return await self.router.generate(messages, complexity=complexity)
        
    async def log_audit(self, tenant_id: str, action_data: Any):
        """Standard wrapper for audit logging."""
        await self.audit.save(tenant_id, self.agent_id, action_data)
