# Use Python base image
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Copy the required files to the container
COPY starsmiles/api/ ./starsmiles/api
COPY starsmiles/ml_logic/ ./starsmiles/ml_logic
COPY models/ ./models
COPY requirements.txt ./requirements.txt

# Install required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "starsmiles.api.fast:app", "--host", "0.0.0.0", "--port", "8000"]
