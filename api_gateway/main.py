from fastapi import FastAPI, Depends, HTTPException, Body
from pydantic import BaseModel
import logging

from api_gateway.security.auth import TokenPayload, require_role
from api_gateway.security.ai_firewall import AIFirewall
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="MIR-Ecosystem API Gateway", version="1.0.0")

# Instrument the FastAPI app for Prometheus metrics
Instrumentator().instrument(app).expose(app)

class TaskRequest(BaseModel):
    prompt: str
    context: dict = {}

@app.get("/health")
async def health_check():
    return {"status": "nominal", "service": "api_gateway"}

@app.post("/api/v1/orchestrator/task", dependencies=[Depends(require_role("Agent-3"))])
async def submit_orchestrator_task(
    request: TaskRequest
):
    """
    Submits a task to the Meta Orchestrator. 
    Requires SUPER_ADMIN role.
    Prompt is scrubbed by AI Firewall.
    """
    AIFirewall.scan_payload(request.prompt)
    # In full implementation, we'd publish this to RabbitMQ here.
    return {"status": "Task accepted by Orchestrator", "trace_id": "mock-trace-id"}

@app.post("/api/v1/financial/analyze", dependencies=[Depends(require_role("Agent-1"))])
async def submit_financial_task(
    request: TaskRequest
):
    """
    Direct access to Agent 1.
    Requires SUPER_ADMIN or FINANCE_EXECUTIVE role.
    """
    AIFirewall.scan_payload(request.prompt)
    return {"status": "Task accepted by Agent 1 (Financial)"}

@app.post("/api/v1/operations/analyze", dependencies=[Depends(require_role("Agent-2"))])
async def submit_operations_task(
    request: TaskRequest
):
    """
    Direct access to Agent 2.
    Requires SUPER_ADMIN or OPS_MANAGER role.
    """
    AIFirewall.scan_payload(request.prompt)
    return {"status": "Task accepted by Agent 2 (Operations)"}
