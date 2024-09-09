.PHONY: docker_build docker_run docker_interactive pylint pytest run_api

docker_build:
	docker build --platform linux/amd64 -t my-fastapi-app:local .

docker_run:
	docker run -d -p 8000:8000 --env-file .env --name my-fastapi-container my-fastapi-app:local

docker_interactive:
	docker run -it --env-file .env my-fastapi-app:local /bin/bash

# TESTS

default: pylint pytest

pylint:
	find . -iname "*.py" -not -path "./tests/*" | xargs -n1 -I {} pylint --output-format=colorized {}; true

pytest:
	PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes

# FAST API

run_api:
	uvicorn starsmiles.api.fast:app --reload
