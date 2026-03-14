# Lung Cancer Detection using CNN

## Author
**Aditya Bhadauria**

---

## Project Overview
This project implements a deep learning model to detect **lung cancer from CT scan images** using a **Convolutional Neural Network (CNN)**.  

The system analyzes CT scan images and classifies them into different categories of lung cancer.

A **Streamlit web application** is also included so users can upload CT scan images and get predictions instantly.

---

## Dataset

Dataset used: **Chest CT-Scan Images Dataset**

Dataset Link:  
https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images

The dataset contains CT scan images categorized into four classes:

- Adenocarcinoma  
- Large Cell Carcinoma  
- Squamous Cell Carcinoma  
- Normal  

---

## Technologies Used :

- Python  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Streamlit  

## Project Structure

```
Lung-Cancer-Detection-CNN
│
├── app.py
├── predict.py
├── train_model.py
├── data_loader.py
├── requirements.txt
├── README.md
│
├── dataset
│
└── model
    └── lung_cancer_model.h5
```

## Installation (Beginner Friendly)

### 1. Clone the Repository
```
git clone https://github.com/ProAdiYT/Lung-Cancer-Detection-CNN.git
```

### 2. Go to Project Folder
```
cd Lung-Cancer-Detection-CNN
```

### 3. Install Required Libraries
```
pip install -r requirements.txt
```

---

## Training the Model

First preprocess the dataset:
```
python data_loader.py
```

Then train the CNN model:
```
python train_model.py
```

After training completes, the trained model file will be saved in the **model** folder.

---

## Running Prediction Script

To test prediction using a sample CT scan image:
```
python predict.py
```

The program will output the predicted lung condition.

---

## Running the Streamlit Web Application

Start the Streamlit app:
```
streamlit run app.py
```
         or
```
python -m streamlit run app.py
```
After running the command, open the browser at:
```
http://localhost:
```

Upload a CT scan image and the system will predict the lung cancer type.

---

## Results

The CNN model achieved approximately **95–99% accuracy** on the validation dataset.

---

## Live Demo

(Add your Streamlit deployment link here after deploying)

Example:
https://lung-cancer-detection-cnn.streamlit.app


---

## Conclusion

This project demonstrates how **deep learning and CNN models can be applied to medical image analysis** for early detection of lung cancer using CT scan images.
