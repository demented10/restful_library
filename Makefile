.PHONY: build up down logs shell db-shell fixtures test

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker-compose exec web bash

db-shell:
	docker-compose exec db psql -U library_user -d library_db

fixtures:
	docker-compose exec web python utils/generate_fixtures.py

test:
	docker-compose exec web python -m pytest

migrate:
	docker-compose exec web alembic upgrade head

# Для локальной разработки без Docker
local-install:
	poetry install

local-run:
	poetry run uvicorn app.main:app --reload
 
local-fixtures:
	poetry run python utils/generate_fixtures.py