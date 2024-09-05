from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import tensorflow as tf

from ml_logic import ImageProcessor, ModelPredictor

app = FastAPI()

# Initialize the processor and predictor
processor = ImageProcessor()
predictor = ModelPredictor('models/dental_model.keras')

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
    prediction = predictor.predict(image_array)
    result = "Positive" if prediction[0] > 0.5 else "Negative"

    return {"prediction": result}

@app.post('/upload_image')
async def receive_image(img: UploadFile = File(...)):
    # Receiving and decoding the image
    contents = await img.read()
    image = Image.open(BytesIO(contents))

    # Preprocess the image
    preprocessed_image = processor.preproc_image(image)

    # Get model prediction
    prediction = predictor.predict(preprocessed_image)

    # Respond with the prediction result as JSON
    return JSONResponse(content={"prediction": prediction})
