# how to capture a webcam inside webcam
# step 1 Import library
import cv2 as cv
import numpy as np

#step 2 Read the frames from camera(webcame)

cap = cv.VideoCapture(0)#webcam no 1

# Step 3 Display Frame by Frame
while(cap.isOpened()):
    #capture frame by frame
    ret,frame = cap.read()
    if ret == True:
        #to display frame
        cv.imshow("Frame", frame)
        # to quite with q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Step 4 : Relese or close all the Windows
cv.waitKey(0)
cv.destroyAllWindows()