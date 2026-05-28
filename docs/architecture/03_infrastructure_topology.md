# 3. Infrastructure Topology & Observability

## 3.1 Infrastructure Overview
The MIR-Ecosystem is designed as a **cloud-native, containerized application**. It will initially use Docker Compose for development and phase into a Kubernetes (K8s) architecture for production deployment to handle high availability and multi-tenant scaling.

## 3.2 Deployment Topology

```mermaid
graph TD
    subgraph External Network
        Users[Web/Mobile Users]
        ThirdParty[Third-Party APIs / BOE / Stripe]
    end

    subgraph Load Balancing & Ingress Layer
        Cloudflare[Cloudflare WAF / CDN]
        Ingress[Nginx Ingress / Traefik]
    end

    subgraph Application Cluster (Kubernetes / Docker Swarm)
        Frontends[Next.js Dashboard Pods]
        APIGateway[FastAPI Gateway Pods]
        
        subgraph Backend Microservices
            AuthSvc[Auth Service]
            BillingSvc[Billing Service]
        end
        
        subgraph AI Execution Cluster (GPU Enabled)
            MetaOrchestrator[Agent 3: Orchestrator]
            FinancialAgent[Agent 1: Financial Workers]
            BIAgent[Agent 2: BI Workers]
            Simulation[Simulation Engine]
        end
    end

    subgraph Message & Data Backbone
        RabbitMQ[RabbitMQ Event Bus]
        Redis[Redis Cache & State]
    end

    subgraph Persistence Storage Layer
        PostgreSQL[(PostgreSQL Primary/Replica)]
        Qdrant[(Vector Database - Qdrant/pgvector)]
        S3[(S3 Compatible Blob Storage)]
    end

    Users --> Cloudflare --> Ingress
    Ingress --> Frontends
    Ingress --> APIGateway
    APIGateway --> AuthSvc
    APIGateway --> RabbitMQ
    
    RabbitMQ <--> MetaOrchestrator
    MetaOrchestrator <--> FinancialAgent
    MetaOrchestrator <--> BIAgent
    
    FinancialAgent --> PostgreSQL
    FinancialAgent --> Qdrant
    BIAgent --> PostgreSQL
    BIAgent --> Qdrant
    
    APIGateway --> Redis
    MetaOrchestrator --> Redis
    
    ThirdParty <--> FinancialAgent
```

## 3.3 Observability Stack
Observability is critical for an AI operating system to trace "why" an AI made a decision, track latency across models, and monitor system health.

1. **Metrics (Prometheus & Grafana)**
   - API latency and error rates.
   - GPU/CPU utilization in the AI Execution Cluster.
   - Token usage and cost tracking per LLM provider.
2. **Distributed Tracing (OpenTelemetry)**
   - Traces requests from the Frontend -> API Gateway -> Orchestrator -> Specific Agent -> LLM Provider -> Database.
   - Critical for debugging complex multi-agent workflows.
3. **Centralized Logging (ELK or Loki)**
   - Audit logs for AI decisions.
   - Structured JSON logging ensuring that all logs have `tenant_id`, `trace_id`, and `agent_id`.

## 3.4 CI/CD Pipeline Design (GitHub Actions)
The deployment lifecycle ensures that the system is stable, versioned, and tested.

1. **Continuous Integration (PR to `develop`)**
   - Linter checks (Ruff for Python, ESLint for Next.js).
   - Type checking (Mypy for Python, TypeScript checks).
   - Unit tests run in isolated containers.
   - *Security Check*: Bandit (Python), npm audit.
2. **Continuous Deployment (Merge to `develop` / `main`)**
   - Build Docker images.
   - Push to Container Registry (GitHub Packages / AWS ECR).
   - Apply database migrations automatically.
   - Deploy to Staging (`develop`) or Production (`main`) via GitOps (ArgoCD or simple webhook).
   - Generate automated changelog and semantic version bump.
