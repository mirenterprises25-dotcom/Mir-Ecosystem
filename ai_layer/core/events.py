from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime
import uuid

class BaseEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    tenant_id: str
    trace_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str
    payload: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None

class TaskRequestedEvent(BaseEvent):
    """
    Emitted by API Gateway to trigger an Orchestrator workflow.
    """
    event_type: str = "TaskRequested"

class AgentSubTaskEvent(BaseEvent):
    """
    Emitted by Orchestrator to trigger specific agents (Agent 1, Agent 2).
    """
    event_type: str = "AgentSubTask"
    target_agent: str

class AgentResponseEvent(BaseEvent):
    """
    Emitted by agents back to the Orchestrator.
    """
    event_type: str = "AgentResponse"
    source_agent: str
    status: str # "success" or "error"

class WorkflowCompletedEvent(BaseEvent):
    """
    Emitted by Orchestrator when the entire synthesis is done.
    """
    event_type: str = "WorkflowCompleted"
