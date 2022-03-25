# Assighnment 
# Change the size of the vedio
# Change the Format

#1-Step Import the Library
import numpy as np
import cv2 as cv

# 
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'WMV1')
out = cv.VideoWriter('resourses/outpu21.mkv', fourcc, 10.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()