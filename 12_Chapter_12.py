# import library 
import cv2 as cv
import numpy as np
# activate the Webcam and capture the video
cap = cv.VideoCapture(0)
cap.set(10, 100)# 10 is the key to set the Brightness
# set the width and height of the video
cap.set(3, 640) #Width 1280
cap.set(4, 480) #Height 1080 for HD
# put the condition to read the webcam video
while(True):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("frame",frame)    # show the display
        if cv.waitKey(1) & 0xFF == ord('q'):    # cose use to quit the video screen
            break
    else:
        break
# relese all the resourses stored in the particular veriables
cap.release()
cv.destroyAllWindows