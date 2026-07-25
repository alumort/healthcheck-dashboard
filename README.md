# HealthCheck Dashboard

HealthCheck Dashboard is a Django-based monitoring system for HTTP services.

The application allows users to register servers, automatically check their availability, measure response times and store monitoring history.

The monitoring system runs asynchronously using Celery workers and scheduled tasks with Celery Beat.

## Tech Stack

- Python 3.12
- Django
- PostgreSQL
- Celery
- Celery Beat
- Redis
- Docker
- Bootstrap 5

## Features

- Server management (Create, Read, Update, Delete)
- HTTP availability monitoring
- Response time measurement
- Status tracking (UP, DOWN, TIMEOUT)
- Health check history
- Background task execution with Celery
- Periodic monitoring with Celery Beat
- PostgreSQL persistence
- Fully Dockerized environment

## Architecture

                +----------------+
                |     Browser    |
                +-------+--------+
                        |
                        v
                 Django Web App
                        |
            +-----------+-----------+
            |                       |
            v                       v
      PostgreSQL                Redis
            ^                       ^
            |                       |
        HealthChecks         Celery Worker
                                   ^
                                   |
                             Celery Beat


## Project Structure
healthcheck/
│
├── config/
│ ├── settings.py
│ ├── celery.py
│ └── urls.py
│
├── servers/
│ ├── models.py
│ ├── views.py
│ ├── tasks.py
│ ├── services.py
│ └── templates/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py


## Running the project

### Clone repository

bash
git clone <repository-url>
cd healthcheck
docker compose build
docker compose up

The application will be available at: 
http://localhost:8000

### Environment
The application uses environment variables for database configuration.

POSTGRES_DB=healthcheck
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

### Database migrations

Run migrations inside the container:
docker compose exec web python manage.py migrate

Create a superuser:
docker compose exec web python manage.py createsuperuser

## What I learned
During this project I learned how to:

During this project I learned how to:

- Build a Django application from scratch
- Design Django models and relationships
- Work with PostgreSQL databases
- Containerize applications using Docker
- Implement asynchronous processing with Celery
- Schedule background jobs with Celery Beat
- Use Redis as a message broker
- Organize a Django project with reusable applications
- Separate business logic into services


## Future Improvements
Possible improvements:

Add monitoring graphs with historical data
Add authentication and user roles
Add API endpoints using Django REST Framework
Add notifications when a service goes down
Add unit and integration tests
