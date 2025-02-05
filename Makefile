#!make
include .env

FAST_API_SRC := app/main.py
FAST_API_OPTS := --host=$(SERVER_HOST) --port=8000

.PHONY: build-run
build-run: build
	docker compose up -d server

.PHONY: run
run:
	fastapi run $(FAST_API_SRC) $(FAST_API_OPTS)

.PHONY: dev
dev:
	fastapi dev $(FAST_API_SRC) $(FAST_API_OPTS)

.PHONY: build
build:
	docker build -t $(SERVER_NAME):$(BUILD_TAG) .

.PHONY: deps
deps: __pyenv__
	pip3 install -r requirements.txt

.PHONY: tests
tests: db-local
	pytest

.PHONY: db-local
db-local:
	docker compose up -d db

.PHONY: down
down:
	docker compose down

.PHONY: lock-deps
lock-deps:
	pip3 freeze > requirements.txt

__pyenv__:
	python3 -m venv __pyenv__

.PHONY: logs
logs:
	docker container logs $(SERVER_NAME)

.PHONY: shell
shell:
	docker exec -it $(SERVER_NAME) /bin/sh

.PHONY: migrate
migrate:
	flask migrate-tables

.PHONY: clean
clean:
	yes | docker container prune
	yes | docker image prune
