.PHONY: up down build test lint format

up:
	docker-compose -f infrastructure/docker/docker-compose.yml up -d

down:
	docker-compose -f infrastructure/docker/docker-compose.yml down

build:
	docker-compose -f infrastructure/docker/docker-compose.yml build

test-backend:
	cd backend && pytest

lint-backend:
	cd backend && ruff check .
	cd backend && mypy .

format-backend:
	cd backend && ruff format .

dev-frontend:
	cd frontend/apps/main-dashboard && npm run dev
