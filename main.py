import cv2
import time
import numpy as np
import glob

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
frames = int(input('Choose how many frames to capture: '))
fpsrender = int(input('Choose the fps for the rendered clip: '))

cv2.namedWindow("test")

img_counter = 0
brek = 0


while True and img_counter < frames:
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        break

    time.sleep(secperframe)
    img_name = "{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    

camera.release()
cv2.destroyAllWindows()
 

img_array = []
for filename in glob.glob('*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fpsrender, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
