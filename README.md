Lung Cancer Detection using CNN

Author: Aditya Bhadauria

Project Overview

This project implements a deep learning system to detect lung cancer from CT scan images using a Convolutional Neural Network (CNN). The model classifies CT scan images into four categories: Adenocarcinoma, Large Cell Carcinoma, Squamous Cell Carcinoma, and Normal.

A Streamlit web interface is included so users can upload a CT image and receive an instant prediction.

Dataset

Dataset used: Chest CT-Scan Images Dataset

Source:
https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images

Classes:

Adenocarcinoma

Large Cell Carcinoma

Squamous Cell Carcinoma

Normal

Technologies Used

Python

TensorFlow / Keras

OpenCV

NumPy

Streamlit

Project Structure
Lung-Cancer-Detection-CNN
│
├── app.py
├── predict.py
├── train_model.py
├── data_loader.py
├── requirements.txt
├── README.md
├── dataset/
└── model/
Installation (Step-by-Step for Beginners)
1. Clone the repository
git clone https://github.com/ProAdiYT/Lung-Cancer-Detection-CNN.git
2. Go to the project folder
cd Lung-Cancer-Detection-CNN
3. Install required libraries
pip install -r requirements.txt
Training the Model

Run the following command to preprocess the dataset:

python data_loader.py

Then train the CNN model:

python train_model.py

After training completes, the trained model file will be created inside the model folder.

Running the Prediction Script

To test prediction on a sample CT scan image:

python predict.py

The program will output the predicted cancer type.

Running the Streamlit Web Application

Start the web interface with:

streamlit run app.py

After running the command, open the browser at:

http://localhost:8501

Upload a CT scan image and the system will predict the lung condition.

Results

The CNN model achieved approximately 95–99% accuracy on the validation dataset.

Live Demo

(Add your Streamlit Cloud deployment link here once the app is deployed.)
