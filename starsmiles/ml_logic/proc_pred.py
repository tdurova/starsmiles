from tensorflow.keras.utils import img_to_array
from PIL import Image

from tensorflow.keras.preprocessing.image import smart_resize
from tensorflow.image import rgb_to_grayscale

def load_image(path_to_image: str)-> Image object:
    return Image.open(path_to_image)

def preproc_image(image: Image) -> Tensor:

    img = img_to_array(image)

    if img.shape[:2]!=(64,64):
        img = smart_resize(img, (64,64))
    if img.shape[2]!=1:
        img = rgb_to_grayscale(img)

    return img

def predict(img: Tensor)-> Str:

    p = np.expand_dims(grey_res_im, axis=0)

    pred = model.predict(p)

    class_names = ['Cavity', 'Fillings', 'Impacted Tooth', 'Implant', 'Normal']

    for i in range(len(pred[0])):
    if round(pred[0,i],0)==1:
        return f'Prediction is {class_names[i]}'
