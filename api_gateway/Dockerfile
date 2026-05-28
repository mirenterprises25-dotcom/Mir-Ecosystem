FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (if any needed for pgvector/psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . /app/api_gateway

# Set Python path so it can resolve api_gateway package
ENV PYTHONPATH=/app

EXPOSE 8000

# Start Uvicorn
CMD ["uvicorn", "api_gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]
