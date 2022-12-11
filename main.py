import cv2
import os
import time

usercam = int(input('Choose camera input (0-5): '))
if usercam == 0:
    camera = cv2.VideoCapture(0)
elif usercam == 1:
    camera = cv2.VideoCapture(1)
elif usercam == 2:
    camera = cv2.VideoCapture(2)
elif usercam == 3:
    camera = cv2.VideoCapture(3)
elif usercam == 4:
    camera = cv2.VideoCapture(4)
elif usercam == 5:
    camera = cv2.VideoCapture(5)
else: 
    camera = cv2.VideoCapture(0)

secperframe = int(input('Choose how many seconds per frame: '))

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    time.sleep(secperframe)
    img_name = "images/{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

camera.release()

cv2.destroyAllWindows()
