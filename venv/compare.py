import csv
from os import path
import os
import cv2
import numpy as np
import face_recognition
from face_recognition.api import face_distance, face_locations
from datetime import datetime
import time
import update
import pickle

classNames = []
encodeListKnown = []


def findEncodings():
    path = "data/encoding"
    myList = os.listdir(path)

    for cl in myList:
        with open(f'{path}/{cl}', 'rb') as input:
            curEnc = pickle.load(input)
        encodeListKnown.append(curEnc)
        classNames.append(os.path.splitext(cl)[0])


def markPresence(name):
    with open("data/attendance.csv", "r+") as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(",")
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{dtString}")
        if name in nameList:
            update.UpdatePresence(name)
        print(myDataList)


findEncodings()
print("Encoding complete")

cap = cv2.VideoCapture(0)

# Get img, convert it, get loc, get encoding
while True:
    # cap = cv2.VideoCapture(0)
    # framerate = cap.get(5)
    success, img = cap.read()
    # cap.release()
    # reduce img size
    img = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation=cv2.INTER_AREA)
    # imga = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faceLocCurFrame = face_recognition.face_locations(img)
    encodeCurFrame = face_recognition.face_encodings(img, faceLocCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceLocCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if (faceDis[matchIndex] < 0.4) and matches[matchIndex]:
            name = classNames[matchIndex]
            markPresence(name)
            print(faceDis[matchIndex])
            print(name)

# cap.release()
# cv2.destroyAllWindows()
        # y1, x1, y2, x2 = faceLoc
        # y1, x1, y2, x2 = y1*4, x1*4, y2*4, x2*4
        # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # cv2.rectangle(img, (x1, y2-35), (x2,y2), (0,255,0), cv2.FILLED)
        # cv2.putText(img, name, (x2-6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    # cv2.imshow("Webcam", img)
    # cv2.waitKey(1)
    # time.sleep(3)

# print(len(encodeListKnown))
