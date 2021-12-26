from os import path
import os
import cv2
import numpy as np
import face_recognition
from face_recognition.api import face_distance, face_locations
from datetime import datetime

# path = "ImagesAttendance"
# images = []
# classNames = []
# myList = os.listdir(path)

# for cl in myList:
#     curImg = cv2.imread(f"{path}/{cl}")
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])

# print("File Read")

# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList

def en():
    encodeList = []
    with open("data/encoding.csv", "r") as f:
        myDataList = f.readlines()
        for line in myDataList:
            entry = line.split(",")
            print(entry[1])
            # encodeList.append(entry[0])
    return encodeList

# output1 = findEncodings(images)
# print(output1)

output2 = en()
print(output2)