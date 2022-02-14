# Load a file from a file and read the File

#import a library 
import cv2 as cv

# load a video in a Veriable
cap = cv.VideoCapture('resourses/video.mkv')
#cap = cv.cvtColor(cap,cv.COLOR_BGR2GRAY)
# Check the Error in the video if there is a error in the file Display the warning code
if(cap.isOpened()==False):
    print("error in reading vedio")


#reading and plying
# apply a while loop on the video
while(cap.isOpened()):# while loop with condition if vedio file load then
    ret, frame = cap.read()# read the video in the veriable
    if ret == True:
        cv.imshow("video",frame)# read the frame in the vedio
        if cv.waitKey(1) & 0xFF == ord('q'):# Video will stop if we press q on the keyboard
            break   # break the loop 
    else:
        break
# veriable in which video load will release the video as it finishes
cap.release()
# close all the windows
cv.destroyAllWindows()