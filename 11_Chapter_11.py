# writing videos from cam
# takes the video from the webcam and make a file and store in the resourses file
import cv2 as cv
import numpy as np
# activatet the webcam and store the video into the cap veriable
cap = cv.VideoCapture(0)
# set the frame width and height 
frame_width = int(cap.get(3))   # width adjustment of the frame 
frame_height = int(cap.get(4))  #height adjustmnet of the frame
# call a veriable out and store all the video format in it
out = cv.VideoWriter('resourses/cam_vedio.avi',cv.VideoWriter_fourcc('M',"j",'P','G'),10,(frame_width,frame_height),isColor=False)
# use the while loop to put the condition
while (True):
    (ret,frame) =  cap.read()# read the video and convert into the frame
    #grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#convert the video ito graycolor
    #(thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)#convert he video into the Binary
    # To Show in Player updated
    if ret == True:
        out.write(frame)
        cv.imshow('Video',frame) # Original image taken from webcam
        if cv.waitKey(1) & 0xFF == ord('q'):    # line of code for quit the display after q press through keyboard
            break
    else:
        break 

cap.release()
cv.destroyAllWindows()