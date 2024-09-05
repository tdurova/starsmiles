import pandas as pd
import numpy as np
import tensorflow as tf
import os

def create_dataset(path_to_directory: str,
                   color_mode='grayscale',
                   class_names=['Cavity', 'Fillings', 'Impacted Tooth', 'Implant', 'Normal'],
                   batch_size=32,
                   image_size=(64,64))-> tf.data.Dataset:
    """Create a dataset from a directory containing
    a set of directories. Each subdirectory contains
    images that will be labeled with the name of the
    subdirectory"""

    ds = tf.keras.preprocessing.image_dataset_from_directory(
    path_to_directory,
    labels='inferred',
    label_mode='int',
    class_names=class_names,
    color_mode=color_mode,
    batch_size=batch_size,
    image_size=image_size,
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True
    )

    return ds

def normalize_ds(ds: tf.data.Dataset)-> tf.data.Dataset:

    """Nomrmalize the values of the image pixels (pixel/255)"""

    ds_norm = ds.map(lambda x, y: (x/255, y))

    return ds_norm
