from prometheus_client import Counter, Histogram

# AI Specific Metrics
llm_token_usage_total = Counter(
    "llm_token_usage_total",
    "Total number of tokens consumed by the LLM Router",
    ["agent", "model_name", "token_type"] # token_type: prompt, completion
)

llm_latency_seconds = Histogram(
    "llm_latency_seconds",
    "Time taken for the LLM to return a response",
    ["agent", "model_name"],
    buckets=(0.5, 1.0, 2.0, 5.0, 10.0, 30.0)
)

# Agent Orchestration Metrics
agent_tasks_total = Counter(
    "agent_tasks_total",
    "Total tasks processed by an agent",
    ["agent", "status"] # status: success, failed, fallback
)

ai_firewall_blocks_total = Counter(
    "ai_firewall_blocks_total",
    "Total number of malicious requests blocked by the AI Firewall",
    ["reason"]
)
