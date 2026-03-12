import os
import cv2
import numpy as np

DATA_DIR = "dataset/train"
IMG_SIZE = 128

categories = [
    "adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib",
    "large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa",
    "normal",
    "squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa"
]

data = []
labels = []

for category in categories:
    
    path = os.path.join(DATA_DIR, category)
    label = categories.index(category)

    for img in os.listdir(path):
        try:
            img_path = os.path.join(path, img)
            image = cv2.imread(img_path)
            image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
            
            data.append(image)
            labels.append(label)

        except Exception:
            pass

data = np.array(data) / 255.0
labels = np.array(labels)

np.save("model/X.npy", data)
np.save("model/y.npy", labels)

print("Dataset processed successfully")