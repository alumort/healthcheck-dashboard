# Architecture

## Components

- Django
- PostgreSQL
- Redis
- Celery Worker
- Celery Beat

## Request Flow

User
↓

Django View
↓

Model

↓

PostgreSQL

Health Check Flow

Celery Beat

↓

Celery Worker

↓

HTTP Request

↓

Save HealthCheck

↓

Dashboard

Folder Structure

config/
    config/
    servers/
    templates/

docs/

Dockerfile

docker-compose.yml