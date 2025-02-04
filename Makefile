#!make
include .env

.PHONY: dev
dev: build
	docker compose up -d server

.PHONY: build
build: $(SERVER_SOURCE)
	docker build -t $(SERVER_NAME):$(BUILD_TAG) .

.PHONY: deps
deps: __pyenv__
	pip3 install -r requirements.txt

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
