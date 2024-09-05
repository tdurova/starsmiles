from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO

from starsmiles.ml_logic.proc_pred import preproc_image, predict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the StarSmiles Model API!"}

@app.post("/predict")
async def predict_endpoint(img: UploadFile = File(...)):
    # Receiving and decoding the image
    contents = await img.read()
    image = Image.open(BytesIO(contents))

    # Preprocess the image
    preprocessed_image = preproc_image(image)

    # Get model prediction
    prediction = predict(preprocessed_image)

    # Respond with the prediction result as JSON
    return JSONResponse(content={"prediction": prediction})
