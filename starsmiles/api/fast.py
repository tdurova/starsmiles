from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf

app = FastAPI()

# Load the pre-trained model
MODEL_PATH = "models/dental_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Define the input data structure using Pydantic
class InputData(BaseModel):
    image: list  # Image data will be passed as a list of pixel values

@app.get("/")
def root():
    return {"message": "Welcome to the StarSmiles Model API!"}

@app.post("/predict")
def predict(input_data: InputData):
    # Convert input to tensor and reshape for model input
    image_array = tf.convert_to_tensor([input_data.image])
    image_array = tf.reshape(image_array, (1, 64, 64, 1))  # Adjust for grayscale image

    # Get model prediction
    prediction = model.predict(image_array)
    result = "Positive" if prediction[0] > 0.5 else "Negative"

    return {"prediction": result}
