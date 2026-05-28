FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/ai_layer

ENV PYTHONPATH=/app

# Default command runs the celery worker.
# We can override this in k8s deployment if we want specific queues per pod
CMD ["celery", "-A", "ai_layer.core.messaging", "worker", "--loglevel=info"]
