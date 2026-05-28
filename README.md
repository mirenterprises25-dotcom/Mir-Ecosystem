# MIR-Ecosystem: Enterprise AI Operating System

Welcome to the MIR-Ecosystem! This repository contains the source code for a centralized, scalable, and cloud-native Enterprise AI Operating System designed specifically for a multi-tenant holding company (MIR Enterprises). 

This OS serves as the "brain" of the enterprise, capable of processing natural language inputs, routing them to specialized AI Agents, and executing workflows across legal, financial, and operational domains.

## 🚀 Quick Start (Local Development)

The entire ecosystem is containerized for easy local deployment.

1. Ensure you have **Docker** and **Docker Compose** installed.
2. Clone this repository and navigate to the root directory.
3. Start the infrastructure and services:
   ```bash
   docker-compose up -d --build
   ```
4. Access the different layers of the system:
   - **Frontend Dashboard:** [http://localhost:3000](http://localhost:3000)
   - **API Gateway (FastAPI Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)
   - **RabbitMQ Management UI:** [http://localhost:15672](http://localhost:15672) (guest/guest)
   - **Grafana Telemetry:** [http://localhost:3001](http://localhost:3001)

## 📚 Documentation Directory

We have provided in-depth documentation to help you understand, maintain, and scale this system. As you grow your coding skills, these documents will serve as a deep-dive reference into the mechanics of the AI OS.

### Architecture & Design
Learn how the system thinks and operates under the hood:
- [System Overview](docs/architecture/01_system_overview.md): High-level view of the 5 layers (Memory, AI, Integration, Simulation, Dashboard).
- [Agent Orchestration & RabbitMQ](docs/architecture/02_agent_orchestration.md): How the AI Agents talk to each other asynchronously.
- [Security & RBAC](docs/architecture/03_security_and_rbac.md): How the API Gateway prevents unauthorized access and stops AI Prompt Injection attacks.

### Developer Guides
Step-by-step guides for working with the code:
- [Developer Setup Guide](docs/guides/developer_setup.md): How to install Python/Node dependencies and run tests locally.
- [Production Deployment](docs/guides/production_deployment.md): How to take the system from Docker Compose to a Kubernetes cloud cluster.
- [API Documentation](docs/api_documentation.md): Static reference for the FastAPI endpoints. *(Note: You can always view the interactive, live API docs by navigating to `/docs` on the running API Gateway).*

## 🛠️ Technology Stack

- **Frontend:** Next.js 15 (React), TailwindCSS, TypeScript
- **Backend API:** FastAPI (Python), PyJWT for Authentication
- **AI Core:** LiteLLM (LLM Routing), Celery (Agent Workers)
- **Message Broker:** RabbitMQ (Asynchronous Event Bus)
- **Memory/Databases:**
  - PostgreSQL (Relational Data & pgvector)
  - Qdrant (Semantic Vector Search)
  - Redis (Fast Caching & Short-term Memory)
- **Observability:** Prometheus, Grafana
- **Infrastructure:** Docker, Kubernetes

## 🔒 Security

The system employs a Zero-Trust architecture at the API Gateway level:
- **JWT (JSON Web Tokens):** Enforces strict Role-Based Access Control (RBAC) and isolates data between different company subsidiaries (Tenant Isolation).
- **AI Firewall:** Scans all incoming AI prompts to block known "jailbreak" attempts and token exhaustion attacks before they reach the expensive LLMs.
