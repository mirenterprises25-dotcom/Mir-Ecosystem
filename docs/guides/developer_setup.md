# Developer Setup Guide

Welcome to the MIR-Ecosystem codebase! This guide will walk you through setting up the environment on your local machine so you can write code, run tests, and understand how the pieces fit together.

## Prerequisites
- **Docker & Docker Compose:** Required to run the infrastructure (RabbitMQ, Postgres, Redis, etc.)
- **Python 3.11+:** For backend and agent development.
- **Node.js 20+:** For frontend Next.js development.
- **Git**

---

## 1. Local Infrastructure

The easiest way to start developing is to spin up the entire backend using Docker Compose.

```bash
# From the root of the repository
docker-compose up -d
```

This command will start:
- PostgreSQL (Port 5432)
- Qdrant Vector DB (Port 6333)
- Redis (Port 6379)
- RabbitMQ (Port 5672, Admin UI: 15672)
- Prometheus & Grafana (Port 9090, 3001)

---

## 2. Running the API Gateway (FastAPI)

While you *can* run the API via Docker, it's often easier to run it locally so you can use debuggers and get hot-reloading.

```bash
# 1. Navigate to the API Gateway
cd api_gateway

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # (On Windows: venv\Scripts\activate)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables (or rely on defaults in main.py)
export PYTHONPATH=".."
export JWT_SECRET="mir_super_secret_dev_key"

# 5. Run the server
uvicorn api_gateway.main:app --reload --port 8000
```
*Visit `http://localhost:8000/docs` to see the interactive Swagger API docs.*

---

## 3. Running the Frontend (Next.js)

The frontend is a React application using the Next.js framework, styled with TailwindCSS.

```bash
# 1. Navigate to the dashboard directory
cd frontend/apps/main-dashboard

# 2. Install dependencies
npm install

# 3. Start the development server
npm run dev
```
*Visit `http://localhost:3000` to see the dark-mode enterprise dashboard.*

---

## 4. Running the Security Tests

We take security seriously. If you make changes to the `api_gateway`, you MUST ensure the AI Firewall and RBAC rules are still working.

```bash
# From the root of the repository
export PYTHONPATH="."
python scripts/test_security.py
```
You should see:
```text
✅ RBAC Test Passed
✅ AI Firewall Test Passed
✅ Access Test Passed
```

## Where to go next?
- Want to add a new Agent? Look inside `ai_layer/agents/`.
- Want to change the JWT rules? Look inside `api_gateway/security/auth.py`.
- Want to tweak the Next.js UI theme? Look at `frontend/apps/main-dashboard/src/components/layout/EnterpriseLayout.tsx`.
