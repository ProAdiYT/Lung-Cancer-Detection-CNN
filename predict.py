import tensorflow as tf
import numpy as np
import cv2

# class labels
categories = [
    "Adenocarcinoma",
    "Large Cell Carcinoma",
    "Normal",
    "Squamous Cell Carcinoma"
]

# load trained model
model = tf.keras.models.load_model("model/lung_cancer_model.h5")

# load test image
img = cv2.imread("test.png")

img = cv2.resize(img, (128,128))
img = img / 255.0
img = np.reshape(img,(1,128,128,3))

# prediction
prediction = model.predict(img)

print("Prediction:", categories[np.argmax(prediction)])