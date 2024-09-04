import tensorflow as tf
from tensorflow.keras import layers, models, callbacks

def build_model(input_shape=(64, 64, 1)):
    """
    Builds a Convolutional Neural Network (CNN) for binary image classification.
    """

    model = models.Sequential()

    # Rescaling layer for normalization
    model.add(layers.InputLayer(input_shape=input_shape))
    model.add(layers.Rescaling(1./255))

    # First Convolutional Block
    model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Second Convolutional Block
    model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Third Convolutional Block
    model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Fourth Convolutional Block
    model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Flatten and Dense Layers
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.5))  # Dropout for regularization

    # Output layer with sigmoid activation for binary classification
    model.add(layers.Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model

def create_callbacks(model_name="model_1"):
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

def train_model(model, train_ds, valid_ds, model_name="model_1", epochs=30):
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
