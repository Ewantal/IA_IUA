import cv2
import numpy as np
from tensorflow import keras
import sys

IMG_WIDTH = 30
IMG_HEIGHT = 30

def load_and_preprocess_image(image_path):
    # Load the image
    new_image = cv2.imread(image_path)
    # Resize the image to match the input size of the model
    new_image = cv2.resize(new_image, (IMG_WIDTH, IMG_HEIGHT))
    # Expand dimensions to create a batch (required by the model)
    new_image = np.expand_dims(new_image, axis=0)
    return new_image

def make_prediction(model, image_path):
    # Load and preprocess the image
    new_image = load_and_preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(new_image)

    # Interpret the predictions (for a classification problem)
    predicted_class = np.argmax(predictions)
    return predicted_class

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python predict.py image_path")

    # Load the trained model
    model = keras.models.load_model('my_model.h5')

    # Path to the image you want to classify
    image_path = sys.argv[1]

    # Make prediction
    predicted_class = make_prediction(model, image_path)

    print(f'The predicted class is: {predicted_class}')
