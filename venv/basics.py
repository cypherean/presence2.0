# import cv2
# # import numpy as np 
# import face_recognition
# from face_recognition.api import face_locations

# # Load image and convert from BGR to RGB
# image_bill = face_recognition.load_image_file('ImagesBasic/bill.jpeg')
# image_bill = cv2.cvtColor(image_bill, cv2.COLOR_BGR2RGB)

# image_test = face_recognition.load_image_file('ImagesBasic/bill2.jpeg')
# image_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2RGB) 

# image_elon = face_recognition.load_image_file('ImagesBasic/elon.jpeg')
# image_elon = cv2.cvtColor(image_elon, cv2.COLOR_BGR2RGB) 

# # Face location to detect loactions - not req at this point
# # Encoding (128 marker) necessary to test
# faceLocBill = face_recognition.face_locations(image_bill)[0]
# encodeBill = face_recognition.face_encodings(image_bill)[0]
# cv2.rectangle(image_bill, (faceLocBill[3], faceLocBill[0]), (faceLocBill[1], faceLocBill[2]), (255,0,255), 2)

# faceLocElon = face_recognition.face_locations(image_elon)[0]
# encodeElon = face_recognition.face_encodings(image_elon)[0]
# cv2.rectangle(image_elon, (faceLocElon[3], faceLocElon[0]), (faceLocElon[1], faceLocElon[2]), (255,0,255), 2)

# faceLocTest = face_recognition.face_locations(image_test)[0]
# encodeTest = face_recognition.face_encodings(image_test)[0]
# cv2.rectangle(image_test, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255), 2)

# # Compare array from DB with test case
# results = face_recognition.compare_faces([encodeBill, encodeElon], encodeTest)
# print(results)

# # Console log func of this test
# cv2.imshow('Bill', image_bill)
# cv2.imshow('Test', image_test)
# cv2.imshow('Elon', image_elon)
# cv2.waitKey(0)