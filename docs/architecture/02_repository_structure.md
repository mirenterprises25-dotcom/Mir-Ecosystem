# 2. Repository Structure & Monorepo Design

## 2.1 Monorepo Architecture Philosophy
The MIR-Ecosystem utilizes a Polyglot Monorepo structure. This ensures that the Frontend (Next.js/TypeScript), Backend (Python/FastAPI), and Infrastructure configurations are versioned together, simplifying CI/CD and ensuring cross-service API compatibility. 

We will use standard directory compartmentalization (Docker Compose based for development) to avoid the heavy overhead of strict JavaScript-centric monorepo tools (like Nx or Turborepo) since our primary backend logic is Python.

## 2.2 File Tree Structure

```text
MIR-Ecosystem/
├── .github/                        # Phase 8: GitHub & Version Control Governance
│   ├── workflows/                  # CI/CD Pipelines (Test, Build, Deploy)
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
│
├── docs/                           # Phase 9: Auto-Documentation System
│   ├── architecture/               # (Current Phase) Architecture Blueprints
│   ├── api/                        # OpenAPI/Swagger generated docs
│   └── guides/                     # Developer onboarding and runbooks
│
├── frontend/                       # Phase 6: Enterprise Dashboards
│   ├── apps/
│   │   ├── main-dashboard/         # Executive Next.js App
│   │   └── client-portal/          # B2B/B2C Next.js App
│   └── packages/                   # Shared UI components & utils
│       ├── ui/                     # Tailwind UI library
│       └── api-client/             # Generated TS clients from backend OpenAPI
│
├── backend/                        # Phase 2: Core Infrastructure
│   ├── api_gateway/                # FastAPI Main Entrypoint
│   ├── services/                   # Microservices
│   │   ├── iam/                    # Identity & Access Management
│   │   ├── billing/                # SaaS Billing & Usage
│   │   └── notifications/          # Email/WebSocket Notifications
│   ├── core/                       # Shared Python Core Logic
│   │   ├── security/               # JWT, RBAC, Encryption
│   │   ├── database/               # SQLAlchemy models & migrations
│   │   └── observability/          # OpenTelemetry setup
│   └── tests/                      # Integration and Unit tests
│
├── ai_layer/                       # Phase 3 & 4: AI Foundation & Agents
│   ├── llm_router/                 # Provider Abstraction (OpenAI, Anthropic, Local)
│   ├── orchestration/              # Agent 3: Meta Orchestrator logic
│   ├── agents/
│   │   ├── agent_financial/        # Agent 1: Financial & Legal
│   │   └── agent_business/         # Agent 2: Operations & BI
│   ├── memory/                     # Memory Management Service (Vector + SQL)
│   └── tools/                      # Shared tools (Scraping, API calls)
│
├── simulation_engine/              # Phase 5: Simulation Framework
│   ├── scenarios/                  # Defined business/tax scenarios
│   └── sandbox/                    # Isolated execution environment
│
├── infrastructure/                 # Deployment & Topology
│   ├── docker/                     # Dockerfiles & docker-compose.yml
│   ├── k8s/                        # Kubernetes manifests / Helm charts
│   ├── terraform/                  # Infrastructure as Code
│   └── observability/              # Prometheus/Grafana configs
│
├── scripts/                        # Automation scripts
├── Makefile                        # Dev commands (e.g., make up, make test)
├── .env.example                    # Environment variables template
├── .gitignore
└── README.md                       # Project root documentation
```

## 2.3 Service Boundaries & Strict Rules
1. **Frontend to Backend**: The `frontend/` apps **MUST ONLY** communicate with the `backend/api_gateway/`. They cannot bypass the gateway to talk directly to services or databases.
2. **Backend to AI Layer**: The `backend/` services invoke the `ai_layer/orchestration/` via message queues (RabbitMQ/Redis) for asynchronous tasks, or via internal gRPC/REST for synchronous queries.
3. **AI Layer Isolation**: Agents (`agent_financial`, `agent_business`) **MUST NOT** communicate directly with each other. All inter-agent communication goes through the `orchestration/` layer (Agent 3).
4. **Database Access**: Each service (IAM, AI Memory, Billing) owns its own tables/schemas. No service may read another service's database directly. They must use internal API calls or event messages.
