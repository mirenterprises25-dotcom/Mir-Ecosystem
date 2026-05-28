import os
from celery import Celery

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

celery_app = Celery(
    "mir_ecosystem_worker",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    # Route tasks to specific queues (Agent 1, Agent 2, Orchestrator)
    task_routes={
        'worker.tasks.orchestrator.*': {'queue': 'orchestrator_queue'},
        'worker.tasks.agent_financial.*': {'queue': 'agent_financial_queue'},
        'worker.tasks.agent_business.*': {'queue': 'agent_business_queue'},
    }
)

# Example task (to be expanded in Phase 3/4)
@celery_app.task(name="worker.tasks.orchestrator.dummy_task")
def dummy_orchestrator_task(task_id: str):
    """
    Stub task for orchestrator execution.
    """
    return {"status": "completed", "task_id": task_id}
