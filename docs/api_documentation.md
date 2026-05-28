# API Documentation

The MIR-Ecosystem uses **FastAPI** to serve its backend endpoints. While FastAPI automatically generates a live, interactive Swagger UI (accessible at `http://localhost:8000/docs` when running locally), this static document serves as a reference guide for the core routes, expected payloads, and security mechanisms.

---

## 🔒 Authentication & Security

All routes require a **Bearer Token (JWT)** in the `Authorization` header.

```http
Authorization: Bearer <your_jwt_token>
```

The JWT payload must contain:
- `user_id`: Unique identifier for the user.
- `tenant_id`: The ID of the subsidiary or tenant. (Strictly enforced for data isolation).
- `role`: Determines access level (`SUPER_ADMIN`, `FINANCE_EXECUTIVE`, `OPS_MANAGER`).

---

## 📡 Endpoints

### 1. Health Check
Checks if the API Gateway is online and responding.

- **URL:** `/health`
- **Method:** `GET`
- **Auth Required:** No

**Response:**
```json
{
  "status": "nominal",
  "service": "api_gateway"
}
```

---

### 2. Meta Orchestrator Task
Submits a complex task to Agent 3 (The Orchestrator). The Orchestrator will analyze the prompt, break it down, and dispatch sub-tasks to Agent 1 and Agent 2 via RabbitMQ.

- **URL:** `/api/v1/orchestrator/task`
- **Method:** `POST`
- **Auth Required:** Yes
- **Allowed Roles:** `SUPER_ADMIN`

**Request Body:**
```json
{
  "prompt": "Analyze the Q4 leather jacket launch considering the new IVA tax rules.",
  "context": {}
}
```

**Security Note:** 
The `prompt` field is scrubbed by the **AI Firewall** middleware. If it exceeds 2000 characters or contains known prompt injection phrases (e.g., "ignore previous instructions"), the request will be rejected with a `400 Bad Request`.

**Success Response (200 OK):**
```json
{
  "status": "Task accepted by Orchestrator",
  "trace_id": "mock-trace-id"
}
```

---

### 3. Financial/Legal Agent Task
Directly submit a task to Agent 1 (Financial/Legal Compliance). Bypasses the Orchestrator.

- **URL:** `/api/v1/financial/analyze`
- **Method:** `POST`
- **Auth Required:** Yes
- **Allowed Roles:** `SUPER_ADMIN`, `FINANCE_EXECUTIVE`

**Request Body:**
```json
{
  "prompt": "Calculate the Impuesto de Sociedades for subsidiary Alpha.",
  "context": {}
}
```

**Success Response (200 OK):**
```json
{
  "status": "Task accepted by Agent 1 (Financial)"
}
```

---

### 4. Operations/BI Agent Task
Directly submit a task to Agent 2 (Operations & Business Intelligence). Bypasses the Orchestrator.

- **URL:** `/api/v1/operations/analyze`
- **Method:** `POST`
- **Auth Required:** Yes
- **Allowed Roles:** `SUPER_ADMIN`, `OPS_MANAGER`

**Request Body:**
```json
{
  "prompt": "Generate a supply chain forecast for next month.",
  "context": {}
}
```

**Success Response (200 OK):**
```json
{
  "status": "Task accepted by Agent 2 (Operations)"
}
```

---

## 📊 Telemetry Metrics
Exposes raw metrics for Prometheus to scrape.

- **URL:** `/metrics`
- **Method:** `GET`
- **Auth Required:** No (usually protected at the network layer in production)
- **Response:** Plain text Prometheus metrics format (e.g., `llm_token_usage_total`, `http_requests_total`).
