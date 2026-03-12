import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model("model/lung_cancer_model.h5")

classes = [
    "Adenocarcinoma",
    "Large Cell Carcinoma",
    "Normal",
    "Squamous Cell Carcinoma"
]

st.title("Lung Cancer Detection using CNN")

file = st.file_uploader("Upload CT Scan Image")

if file is not None:
    
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    img = cv2.resize(img,(128,128))
    img = img/255.0
    img = np.reshape(img,(1,128,128,3))
    
    prediction = model.predict(img)
    
    result = classes[np.argmax(prediction)]
    
    st.image(file)
    st.write("Prediction:", result)