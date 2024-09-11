.PHONY: docker_build docker_run docker_interactive pylint pytest run_api

# Define the Docker image name as a variable
IMAGE_NAME = my-fastapi-app:local

# Build Docker image if not built yet
docker_build:
	docker build --platform linux/amd64 -t $(IMAGE_NAME) .

# Run Docker container in detached mode
docker_run:
	docker run -d -p 8000:8000 --env-file .env --name my-fastapi-container $(IMAGE_NAME)

# Run Docker container interactively (to enter bash shell)
docker_interactive:
	docker run -it --env-file .env $(IMAGE_NAME) /bin/bash

# Run pylint inside Docker container
pylint:
	docker run -it --rm $(IMAGE_NAME) sh -c "find . -iname '*.py' -not -path './tests/*' | xargs pylint"

# Run pytest inside Docker container
pytest:
	docker run -it --rm $(IMAGE_NAME) sh -c "PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes"

# Run FastAPI inside Docker container
run_api:
	docker run -d -p 8000:8000 --env-file .env --name my-fastapi-container $(IMAGE_NAME) uvicorn starsmiles.api.fast:app --reload
