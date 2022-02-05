#reading a video 

#import a library 
import cv2 as cv
from sqlalchemy import false

# load a video into the code
cap = cv.VideoCapture('resourses/vedio.mp4')

if(cap.isOpened()==False):
    print("error in reading vedio")


#reading and plying

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("video",frame)
        cv.waitKey(0)
    else:
        break
cap.release()
cv.destroyAllWindows()