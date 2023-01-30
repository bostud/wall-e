
build:
	docker-compose build app postgres_db redis

run:
	docker-compose up app

rebuild:
	docker-compose up --build --force-recreate app

migrate:
	docker exec walle_app python run_migrations.py

dev-test:
	docker exec walle_app pytest -v tests/
