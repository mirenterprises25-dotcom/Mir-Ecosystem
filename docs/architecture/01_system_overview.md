# 1. System Overview & Enterprise Architecture

## 1.1 Executive Summary
The **MIR-Ecosystem** is a centralized, cloud-native Enterprise AI Operating System designed to manage a multi-tenant holding company structure (MIR Enterprises, MIR Consulting, MIR Clothing, MIR Commerce, and future subsidiaries). It goes beyond standard automation tools to act as a cognitive governor for business operations, financial compliance, legal intelligence, and trend forecasting.

## 1.2 Multi-Tenant SaaS Structure Mapping
The system uses a hierarchical multi-tenant architecture designed to scale globally.

```mermaid
graph TD
    System[MIR-Ecosystem Platform Core] --> Holding[MIR Enterprises (Root Tenant)]
    
    Holding --> Sub1[MIR Consulting]
    Holding --> Sub2[MIR Clothing]
    Holding --> Sub3[MIR Commerce]
    Holding --> SubN[Future Subsidiaries]
    
    Sub1 --> Client1A[External Client A]
    Sub1 --> Client1B[External Client B]
    
    Sub3 --> StoreA[B2C Store]
    Sub3 --> StoreB[B2B Partner Portal]
```

## 1.3 High-Level Enterprise Architecture
The system consists of several decoupled layers ensuring scalability, fault tolerance, and modularity.

```mermaid
flowchart TB
    subgraph Presentation Layer [Phase 6: Enterprise Dashboards]
        UI[Next.js / React Web App]
        Mobile[Future Mobile App]
        API_GW_EXT[External API Gateway]
    end

    subgraph API & Routing Layer [Phase 2: Core Infrastructure]
        Nginx[Nginx / Ingress Controller]
        API_GW[FastAPI Gateway]
        Auth[Auth Service - JWT/OAuth2]
    end

    subgraph AI Foundation Layer [Phase 3 & 4]
        LLM_Router[LLM Abstraction & Routing Layer]
        Agent1[Financial & Legal AI]
        Agent2[Operations & BI AI]
        Agent3[Meta Orchestrator & Governor]
    end

    subgraph Execution & Event Layer
        EventBus[RabbitMQ / Redis Streams]
        Workers[Celery / Async Workers]
        Simulation[Phase 5: Simulation Engine]
    end

    subgraph Data & Memory Layer
        SQL[(PostgreSQL - Relational)]
        Vector[(pgvector / Qdrant - Semantic)]
        Cache[(Redis - Caching)]
        Logs[(OpenSearch / TimescaleDB - Audit)]
    end

    Presentation Layer --> Nginx
    Nginx --> API_GW
    API_GW <--> Auth
    
    API_GW --> Agent3
    API_GW --> EventBus
    
    Agent3 --> Agent1
    Agent3 --> Agent2
    Agent3 --> LLM_Router
    
    Agent1 <--> EventBus
    Agent2 <--> EventBus
    Simulation <--> EventBus
    Workers <--> EventBus
    
    Agent1 --> SQL
    Agent1 --> Vector
    Agent2 --> SQL
    Agent2 --> Vector
    Agent3 --> Logs
    Workers --> Cache
```

## 1.4 Service Boundaries & Microservice Relationships

To maintain loose coupling, the system is divided into domain-driven microservices:

1. **Identity & Access Management (IAM) Service**: Handles authentication, RBAC/ABAC, and multi-tenant isolation.
2. **Core API Gateway**: Routes external requests to appropriate internal microservices.
3. **Agent Orchestration Service**: The execution environment for Agent 3 (Meta Orchestrator) to spawn, monitor, and kill sub-agents.
4. **Financial & Legal Domain Service (Agent 1)**: Interfaces with external legal endpoints (BOE Spain, Agencia Tributaria), performs scraping, and updates the compliance vector store.
5. **Business Intelligence Domain Service (Agent 2)**: Integrates with e-commerce data streams, social media APIs, and product databases.
6. **Simulation Engine Service**: A sandboxed environment for running "what-if" business scenarios without polluting production data.
7. **Memory Management Service**: Provides a unified API for agents to read/write from Short-Term, Long-Term, Structured, and Audit memories.

## 1.5 Technology Stack Overview
- **Frontend**: Next.js, React, TypeScript, TailwindCSS
- **Backend**: Python 3.11+, FastAPI (Async), Pydantic
- **AI/LLM**: LangChain/LlamaIndex (Custom Abstraction), OpenAI/Anthropic/Local Integrations
- **Database**: PostgreSQL 16 (Relational), pgvector/Qdrant (Vector), Redis (Cache/Queue)
- **Messaging**: RabbitMQ / Redis Streams
- **Infrastructure**: Docker, Kubernetes, Nginx, GitHub Actions
- **Observability**: Prometheus, Grafana, OpenTelemetry
