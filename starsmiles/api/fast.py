from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO

from starsmiles.proc_pred import preprocess_image, predict

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
    preprocessed_image = preprocess_image(image)

    # Get model prediction
    prediction = predict(preprocessed_image)

    print(prediction)

    # Respond with the prediction result as JSON
    return JSONResponse(content={"cavity": float(prediction[0][0]),
                                 'fillings': float(prediction[0][1]),
                                 'impacted tooth': float(prediction[0][2]),
                                 'implant': float(prediction[0][3]),
                                 'normal': float(prediction[0][4])})
