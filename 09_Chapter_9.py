# how to capture a webcam inside webcam

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)#webcam no 1

#if (cap.isOpend()==False):
 #   print("there is error")
# read untill the end

while(cap.isOpened()):
    #capture frame by frame
    ret,frame = cap.read()
    if ret == True:
        #to display frame
        cv.imshow('frame',frame)
        # to quite with q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    
cv.waitKey(0)
cv.destroyAllWindows()