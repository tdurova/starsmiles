import os
import logging
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.preprocessing.image import smart_resize
from tensorflow.image import rgb_to_grayscale

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the model path from the environment variable
root_path = os.path.dirname(os.path.dirname(__file__))

model_path = os.path.join(root_path, 'models', 'model.keras')

print(model_path)

# Check if the model file exists
if not model_path or not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

# Load your pre-trained model
model = tf.keras.models.load_model(model_path)

def load_image(image_path: str) -> Image.Image:
    """
    Load the image to predict.

    Args:
        image_path (str): Path to the image file.

    Returns:
        Image.Image: Loaded image.
    """
    try:
        return Image.open(image_path)
    except Exception as e:
        logging.error("Error loading image: %s", e)
        raise

def preprocess_image(image: Image.Image) -> tf.Tensor:
    """
    Preprocess the image to make it compatible with the model.

    Args:
        image (Image.Image): Image to preprocess.

    Returns:
        tf.Tensor: Preprocessed image tensor.
    """
    try:
        img_array = img_to_array(image)

        # Resize image if necessary
        if img_array.shape[:2] != (64, 64):
            img_array = smart_resize(img_array, (64, 64))

        # Convert to grayscale if necessary
        if img_array.shape[2] != 1:
            img_array = rgb_to_grayscale(img_array)

        return img_array
    except Exception as e:
        logging.error("Error preprocessing image: %s", e)
        raise

def predict(image_tensor: tf.Tensor, threshold: float = 0.5) -> str:
    """
    Make a prediction with the preprocessed image and return the results.

    Args:
        image_tensor (tf.Tensor): Preprocessed image tensor.
        threshold (float): Probability threshold to consider predictions valid.

    Returns:
        str: Prediction result with class name and probability.
    """
    try:
        # Expand dimensions to match model input
        input_tensor = np.expand_dims(image_tensor, axis=0)
        predictions = model.predict(input_tensor)

        return predictions

        class_names = ['Cavity', 'Fillings', 'Impacted Tooth', 'Implant', 'Normal']
        best_prediction = None
        best_probability = 0.0

        # Iterate over predictions to find the best one above the threshold
        for i, probability in enumerate(predictions[0]):
            logging.info("Probability of %s: %.2f%%", class_names[i], probability * 100)

            # Only consider predictions above the specified threshold
            if probability > threshold and probability > best_probability:
                best_probability = probability
                best_prediction = class_names[i]

        if best_prediction:
            return f"Prediction: {best_prediction} with a probability of {best_probability * 100:.2f}%"
        return "The model cannot predict with enough confidence."
    except Exception as e:
        logging.error("Error during prediction: %s", e)
        raise
