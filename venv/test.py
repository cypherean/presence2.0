from os import PRIO_PGRP, path
import os
import cv2
import numpy as np
import face_recognition
from datetime import datetime
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))

path = "data/images"
images = []
classNames = []
myList = os.listdir(path)

for _, dirs, _ in os.walk(path):
    for dir in dirs:
        print(dir)
        for _, _, files in os.walk(os.path.join(path,dir)):
            for cl in files:
                # print(cl)
                curImg = cv2.imread(str(os.path.join(path,dir,cl))+".jpeg")
                print(curImg)
                images.append(curImg)
                classNames.append(str(dir))
print(images)

print("Folder Read")

# def getEncodingLen():
#     with open("data/attendance.csv", "r") as f:
#         myDataList = f.readlines()
#     return len(myDataList)

# if (len(myList) != (getEncodingLen()-1)):
#     print('unequal')


# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList


# def storeEncodings():
#     encodeList = findEncodings(images)
#     print(cross_val_score(clf, np.array(encodeList), np.array(classNames), cv=5, scoring='accuracy_score'))

#     clf.fit(np.array(encodeList), np.array(classNames))
#     with open(f'data/encoding/clf.pkl', "wb") as output:
#     # np.save(f"data/encoding/{name}.npy", encode)
#         pickle.dump(clf, output, pickle.HIGHEST_PROTOCOL)


# storeEncodings()

#print("Encoding Done")
