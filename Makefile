build:
	docker-compose build

up:
	docker-compose up -d

logs:
	docker-compose logs -f

test:
	docker-compose run --rm --no-deps --entrypoint="python -m pytest" api /code/tests

down:
	docker-compose down --remove-orphans

all: down build up test