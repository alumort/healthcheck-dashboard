build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

restart:
	docker compose restart web

migrate:
	docker compose exec web python manage.py migrate

migrations:
	docker compose exec web python manage.py makemigrations

shell:
	docker compose exec web python manage.py shell

createsuperuser:
	docker compose exec web python manage.py createsuperuser