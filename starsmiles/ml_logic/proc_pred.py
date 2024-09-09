import os
import numpy as np
from tensorflow.keras.utils import img_to_array
from PIL import Image
from tensorflow.keras.preprocessing.image import smart_resize
from tensorflow.image import rgb_to_grayscale
import tensorflow as tf

# Load the model path from the environment variable
model_path = os.getenv('MODEL_PATH')

# Check if the model file exists
if not model_path or not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

# Load your pre-trained model
model = tf.keras.models.load_model(model_path)

def load_image(path_to_image: str) -> Image.Image:
    return Image.open(path_to_image)

def preproc_image(image: Image.Image) -> tf.Tensor:
    img = img_to_array(image)

    if img.shape[:2] != (64, 64):
        img = smart_resize(img, (64, 64))
    if img.shape[2] != 1:
        img = rgb_to_grayscale(img)

    return img

def load_model():
    from tensorflow.keras.models import load_model
    return load_model(model_path)

def predict(img: tf.Tensor) -> str:
    p = np.expand_dims(img, axis=0)
    pred = model.predict(p)

    class_names = ['Cavity', 'Fillings', 'Impacted Tooth', 'Implant', 'Normal']
    threshold = 0.5
    prediction = None
    probability = 0.0

    for i in range(len(pred[0])):
        # print(f'Probability of {class_names[i]}: {round(100 * pred[0, i], 2)}%')

        if pred[0, i] > threshold:
            threshold = pred[0, i]
            prediction = class_names[i]
            probability = pred[0, i]

    if prediction is not None:
        return f'Prediction is: {prediction} with a probability of {round(100 * probability, 2)}%'
    else:
        return 'The model can not predict with enough confidence'
