#

import cv2 as cv
import numpy as np
from tkinter import Frame

cap = cv.VideoCapture(0)

while(True):
    (ret,frame)= cap.read()
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binaryimg) = cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)

    cv.imshow("original",frame)
    cv.imshow("GrayCam",gray_frame)
    cv.imshow("GrayCam",binaryimg)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break

cv.waitKey(0)
cv.destroyAllWindows()