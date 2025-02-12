.DEFAULT_GOAL = run

run:
	docker compose up

run-d:
	docker compose up -d

run-build:
	docker compose up --build

build:
	docker compose build

stop:
	docker compose stop

down:
	docker compose down --remove-orphans -v

mm:
	docker compose run --rm api python manage.py migrate

mkm:
	docker compose run --rm api python manage.py makemigrations

mkm-m: mkm mm

bash:
	docker compose run --rm --entrypoint="" api sh

lint:
	flake8 fastapi/
