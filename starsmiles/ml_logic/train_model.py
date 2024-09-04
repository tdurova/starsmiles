from modeling import build_model, train_model
import tensorflow as tf

# Build the model
model = build_model()

# Train the model
history = train_model(model, train_ds, valid_ds, model_name="model_1", epochs=30)
