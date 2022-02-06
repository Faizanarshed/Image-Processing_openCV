# Assighnment
#Import Library
import numpy as np #numpy for array
import cv2 as cv    #cv2 for openCV

cap = cv.VideoCapture(0)    #activate the WebCam

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'MJPG') #Set the Video Format
out = cv.VideoWriter('resourses/output1.avi', fourcc, 20.0, (640,  480))   #Video format and location of file where he will save
while cap.isOpened():
    ret, frame = cap.read() # Read the webcam convert it into frames
    frame = cv.flip(frame, 1) # frame on flip 0 image will be 180 deg rotate
    # write the flipped frame
    out.write(frame)    #save the frame or video
    cv.imshow('frame', frame) #Image show 
    if cv.waitKey(1) == ord('q'): # wait key it will not let the disparse ina second
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()