# set the resulution of the webcam
# Resolution of webcam
# import the libraries
import cv2 as cv
import numpy as np
from tblib import Frame
#    create a veriable where we store the cam video
cap = cv.VideoCapture(0)

#   set the Webcam Resolution into HD
#cap.set(3,1280)
#cap.set(4,720)
# Set the Video resolution into HD Format
# HD Video with an aspect ratio (AR) of 16:9
def hd_resolution():
    cap.set(3, 1280)    # 1280 columns
    cap.set(4, 720)     #  720 horizontal lines
    # set the resolution into SD Format
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)
    # set the Resolution into 4K
def fhd_resolution():
    cap.set(3, 1920)    # 1920 Columns
    cap.set(4, 1080)    #1080 Horizontal lines
# how to change and fix the frame 30fph
#hd_resolution()
#sd_resolution()
fhd_resolution
while(True):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("camera",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()