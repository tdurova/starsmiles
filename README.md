# StarSmiles: AI-Powered Dental Radiography Classification API

StarSmiles is a deep learning-powered API designed to classify dental X-rays, automating the detection of conditions like cavities, implants, and impacted teeth. Developed during the Le Wagon bootcamp, this project highlights my skills as a **Machine Learning Engineer** with strong **backend development** and **project management** experience.

## Key Highlights

- **Automated Dental Diagnosis**: Classifies X-rays into dental conditions (Cavity, Fillings, Implants, etc.).
- **FastAPI Integration**: Exposes the model via a production-ready API for seamless integration with dental clinics.
- **Efficient Preprocessing & Training**: Custom pipeline to handle and preprocess dental X-ray images.
- **Scalable Architecture**: Designed for future improvements, retraining, and deployment with Docker.

## Installation & Usage

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/project-starsmiles.git
   cd project-starsmiles
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Run the API:**
   ```
   uvicorn starsmiles.api.fast:app --reload
   ```
4. **Use the API:** Send a POST request with an X-ray image to `/predict`.

## Building and Running Docker Locally

### Prerequisites

**Ensure you have Docker installed on your machine. You can download and install Docker from **[here](https://www.docker.com/products/docker-desktop).

### Step 1: Update Environment Variables

**Ensure your **`.env` file contains the correct paths and environment variables. Here is an example:

```
TRAIN_DATA_DIR=raw_data/Dental_Radiography/train
TEST_DATA_DIR=raw_data/Dental_Radiography/test
VALID_DATA_DIR=raw_data/Dental_Radiography/valid
MODEL_PATH=/app/models/model.keras
```

### Step 2: Build Docker Image

**Navigate to the root directory of your project and run the following command to build the Docker image:**

```
make docker_build
```

### Step 3: Run Docker Container

**Run the Docker container using the following command:**

```
make docker_run
```

### Step 4: Verify Docker Container

**Check the logs to ensure the application is running correctly:**

```
docker logs my-fastapi-container
```

### Step 5: Access Application

**Open a web browser and navigate to **`http://localhost:8000` to access your FastAPI application. You can also check the automatically generated API documentation at `http://localhost:8000/docs`.

### Example Commands

**Here are the example commands you should run from the root of your project directory:**

1. **Build Docker Image**:
   ```
   make docker_build
   ```
2. **Run Docker Container**:
   ```
   make docker_run
   ```
3. **Check Logs**:
   ```
   docker logs my-fastapi-container
   ```
4. **Access Application**: Open a web browser and navigate to `http://localhost:8000`.

**By following these steps, you should be able to build and run your Docker container locally.**
