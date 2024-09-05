import tensorflow as tf
from tensorflow.keras import layers, callbacks, _optimizers
from tf.keras.models import Model, Sequential

def build_model(input_shape=(64, 64, 1)):
    """
    Builds a Convolutional Neural Network (CNN) for binary image classification.
    """

    model = Sequential()

    # Define the input shape explicitly using Input
    model.add(Input(shape=input_shape))

    # Rescaling layer for grayscale images
    model.add(layers.Rescaling(1./255))

    # First Convolutional Block
    model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same"))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))

    #Second Convolutional Block
    model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same"))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))

    # Third Convolutional Block
    model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))

    # Fourth Convolutional Block
    model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))

    # Flattening the output
    model.add(layers.Flatten())

    # Fully Connected Dense Layer
    model.add(layers.Dense(64, activation="relu"))

    # Dropout Layer for regularization
    model.add(layers.Dropout(0.5))

    # Output Layer with Softmax
    model.add(layers.Dense(5, activation="softmax"))

    return model

def compile_model(model):
    adam = optimizers.Adam(learning_rate = 0.001)
    return model.compile(loss='categorical_crossentropy',
              optimizer= adam,
              metrics=['accuracy'])

def create_callbacks(model_name="model"):
    """
    Creates a list of callbacks for training.
    """

    model_checkpoint = callbacks.ModelCheckpoint(f"{model_name}.h5",
                                                 monitor="val_loss",
                                                 save_best_only=True)

    lr_reducer = callbacks.ReduceLROnPlateau(monitor="val_loss",
                                             factor=0.1,
                                             patience=3,
                                             verbose=1,
                                             min_lr=1e-6)

    early_stopper = callbacks.EarlyStopping(monitor='val_loss',
                                            patience=10,
                                            verbose=1,
                                            restore_best_weights=True)

    return [model_checkpoint, lr_reducer, early_stopper]

def train_model(model, train_ds, valid_ds, model_name="mode1", epochs=30):
    """
    Trains the CNN model using the provided training and validation datasets.
    """

    # Create the callbacks
    callbacks_list = create_callbacks(model_name)

    # Train the model
    history = model.fit(
        train_ds,
        epochs=epochs,
        validation_data=valid_ds,
        callbacks=callbacks_list
    )

        # Save the model
    MODEL_PATH = "../models/model.h5"
    model.save(MODEL_PATH)

    return history
