import numpy as np
import tensorflow as tf

def predict(model, image_path, image_size=(64, 64)):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=image_size, color_mode='grayscale')
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale like during training

    prediction = model.predict(img_array)
    return prediction
