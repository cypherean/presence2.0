from os import path
import os
import cv2
import numpy as np
import face_recognition
from datetime import datetime

path = "data/dataset"
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f"{path}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print("Folder Read")

# def getEncodingLen():
#     with open("data/attendance.csv", "r") as f:
#         myDataList = f.readlines()
#     return len(myDataList)

# if (len(myList) != (getEncodingLen()-1)):
#     print('unequal')


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def storeEncodings():
    encodeList = findEncodings(images)
    for name, encode in zip(classNames, encodeList):
        np.save(f"data/encoding/{name}.npy", encode)


storeEncodings()

print("Encoding Done")
