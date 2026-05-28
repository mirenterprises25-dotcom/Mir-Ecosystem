# Production Deployment Guide (Kubernetes)

When you are ready to move the MIR-Ecosystem out of `docker-compose` and into a highly available cloud environment, you will use the Kubernetes (K8s) manifests located in `infrastructure/k8s/`.

This guide assumes you have a running Kubernetes cluster (e.g., AWS EKS, Google GKE, or Azure AKS) and `kubectl` configured.

## 1. Secrets Management

Before deploying any pods, you must create a Kubernetes Secret to hold sensitive information like API keys and database passwords. **Never commit these to version control.**

```bash
kubectl create secret generic mir-secrets \
  --from-literal=jwt-secret="YOUR_PRODUCTION_JWT_SECRET" \
  --from-literal=litellm-api-key="YOUR_PROVIDER_API_KEY" \
  --from-literal=database-url="postgresql://user:pass@host:5432/db" \
  --from-literal=rabbitmq-url="amqp://user:pass@host:5672/"
```

## 2. Infrastructure Deployment

You need to provision your managed databases (Postgres, Redis, Qdrant, RabbitMQ) via your cloud provider or Helm charts. 

Once the infrastructure URLs are updated in your `mir-secrets`, apply the application manifests:

```bash
# 1. Deploy the API Gateway (2 replicas)
kubectl apply -f infrastructure/k8s/api-gateway.yaml

# 2. Deploy the Next.js Frontend (2 replicas)
kubectl apply -f infrastructure/k8s/frontend.yaml

# 3. Deploy the AI Celery Workers (3 replicas)
kubectl apply -f infrastructure/k8s/agents.yaml
```

## 3. Ingress Routing (NGINX & SSL)

The `ingress.yaml` file configures NGINX to route external HTTP traffic to your internal `ClusterIP` services. It also requests SSL certificates via `cert-manager`.

```bash
# Apply the Ingress configuration
kubectl apply -f infrastructure/k8s/ingress.yaml
```

- `dashboard.mir-ecosystem.com` -> Routes to the Next.js frontend.
- `api.mir-ecosystem.com` -> Routes to the FastAPI gateway.

## 4. CI/CD Automation

You don't need to manually build Docker images. The repository contains a GitHub Actions workflow (`.github/workflows/ci.yml`).
When you merge code into the `main` branch, the pipeline will:
1. Run linting and security tests.
2. Build optimized Docker images for the Frontend, API, and AI Workers.
3. Push those images to the GitHub Container Registry (`ghcr.io`).

To deploy an update, simply rollout a restart to your deployments to pull the latest image:
```bash
kubectl rollout restart deployment api-gateway
kubectl rollout restart deployment frontend-dashboard
kubectl rollout restart deployment agent-worker
```
