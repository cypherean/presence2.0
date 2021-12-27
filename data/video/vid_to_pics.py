import cv2
vidcap = cv2.VideoCapture('vid1.mp4')
if vidcap.isOpened():
  print("tst")
#     current_frame = 0
#     while True:
#         ret, frame = vidcap.read()
#         if ret: 
#             name = f'frameIn/frame{current_frame}.jpg'
#             print(f"Creating file... {name}")
#             cv2.imwrite(name, frame)
#             frames.append(name)
#         current_frame += 1
#     cap.release()
# cv2.destroyAllWindows()
# success, image = vidcap.read()
# count = 1


# while True:
#   print("test")
#   cv2.imwrite("video_data/image_%d.jpg" % count, image)    
#   success, image = vidcap.read()
#   print('Saved image ', count)
#   count += 1
