gar_creation:
  gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev
  gcloud artifacts repositories create ${GAR_REPO} --repository-format=docker \
  --location=${GCP_REGION} --description="Repository for storing ${GAR_REPO} images"

docker_build:
  docker build --platform linux/amd64 -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod .

docker_push:
  docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod

docker_run:
  docker run -e PORT=8000 -p 8000:8000 --env-file .env ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod

docker_interactive:
  docker run -it --env-file .env ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod /bin/bash

docker_deploy:
  gcloud run deploy --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod --memory ${GAR_MEMORY} --region ${GCP_REGION}

#TESTS

default: pylint pytest

pylint:
    find . -iname "*.py" -not -path "./tests/*" | xargs -n1 -I {}  pylint --output-format=colorized {}; true

pytest:
    PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes

#FAST API

fast_api:
		uvicorn starsmiles.api.fast:app --reload
