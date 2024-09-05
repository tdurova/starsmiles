import numpy as np

from tensorflow.keras.utils import img_to_array
from PIL import Image
from tensorflow.keras.preprocessing.image import smart_resize
from tensorflow.image import rgb_to_grayscale
import numpy as np
import tensorflow as tf

# Load your pre-trained model (adjust the path as necessary)
model = tf.keras.models.load_model('models/model.keras')

def load_image(path_to_image: str)-> Image:
    return Image.open(path_to_image)

def preproc_image(image: Image):

    img = img_to_array(image)

    if img.shape[:2] != (64, 64):
        img = smart_resize(img, (64, 64))
    if img.shape[2] != 1:
        img = rgb_to_grayscale(img)

    return img

def load_model():
    from tensorflow.keras.models import load_model

    return load_model('/home/enric/code/tdurova/starsmiles/model/model.keras',)

def predict(img, model=load_model())->None:

    p = np.expand_dims(img, axis=0)

    pred = model.predict(p)

    class_names = ['Cavity', 'Fillings', 'Impacted Tooth', 'Implant', 'Normal']

    threshold = 0.5
    for i in range(len(pred[0])):
        print(f'Probability of {class_names[i]}: {round(100*pred[0,i],2)}%')

        if pred[0,i]>threshold:
            threshold=pred[0,i]
            prediction = class_names[i]

    if prediction is not None:
        print(f'Prediction is: {prediction}')
    else:
        print('The model can not predict with enough confidence')
