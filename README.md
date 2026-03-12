# Lung Cancer Detection using CNN

## Author
Aditya Bhadauria

## Project Description
This project detects lung cancer from CT scan images using a Convolutional Neural Network (CNN). The model analyzes CT scan images and classifies them into different categories of lung cancer.

## Dataset

The model was trained using the **Chest CT-Scan Images Dataset** available on Kaggle.

Dataset link:  
https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images

The dataset contains CT scan images categorized into four classes:

- Adenocarcinoma
- Large Cell Carcinoma
- Squamous Cell Carcinoma
- Normal

The dataset is organized into training, validation, and testing folders.
Images were resized to 128×128 pixels before training the CNN model.

## Technologies Used
- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Streamlit

## Methodology
1. CT scan images are collected from the dataset.
2. Images are resized to 128x128 pixels.
3. Data preprocessing is done using NumPy and OpenCV.
4. A Convolutional Neural Network (CNN) is built using TensorFlow/Keras.
5. The model is trained on CT scan images.
6. The trained model predicts lung cancer type.
7. A Streamlit web app allows users to upload CT images and get predictions.

## Results
The CNN model achieved around **95–99% accuracy** on the validation dataset.

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Live Application
(Add your Streamlit deployment link here after deployment)