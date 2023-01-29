
build:
	docker-compose build app postgres_db redis

run:
	docker-compose up app

rebuild:
	docker-compose up --build --force-recreate app

migrate:
	docker exec walle_app python run_migrations.py

tests:
	docker-compose up -d --build test_app test_postgres_db test_redis
	docker exec walle_test_app python run_migrations.py
	docker exec walle_test_app pytest tests/
	docker container rm --force --volumes walle_test_app walle_test_postgres_db walle_test_redis

dev-test:
	docker exec walle_app pytest tests/
