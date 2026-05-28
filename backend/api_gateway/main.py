from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

app = FastAPI(
    title="MIR-Ecosystem API",
    description="Enterprise AI Operating System Core API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health")
async def health_check() -> Dict[str, Any]:
    """
    Basic health check endpoint to verify API Gateway is running.
    """
    return {
        "status": "healthy",
        "service": "api_gateway",
        "version": "0.1.0"
    }

@app.get("/api/v1/system/status")
async def system_status() -> Dict[str, Any]:
    """
    Returns the status of the entire ecosystem (Agents, Database, Memory).
    (Stub implementation for Phase 2)
    """
    return {
        "status": "online",
        "components": {
            "database": "connected",
            "redis": "connected",
            "rabbitmq": "connected",
            "agent_orchestrator": "idle",
            "simulation_engine": "offline"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
