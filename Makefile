SHELL := /bin/bash
MAX_LINE_LENGTH := 119
COMPOSE_VERSION := $(shell docker-compose --version 2>/dev/null)
DOCKER_VERSION := $(shell docker --version 2>/dev/null)

help: ## List all commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9 -_]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

###################################################################################################
# docker

logs: ## Display and follow docker logs
	docker compose logs --tail=500 --follow

build: ## Update/Build docker services
	docker-compose pull
	docker-compose build --pull

down: ## Start docker containers
	docker compose down

up: ## Start docker containers
	docker compose up
	#$(MAKE) logs

bash: ## Open a bash in container
	@docker compose exec schedules_app_1 bash

styles: ## Executes flake8, black and isort checks
	@poetry run scripts/lint.sh

test: ## Executes test
	@PYTHONPATH=app poetry run pytest --cov=tests --cov=app --cov-config=setup.cfg
