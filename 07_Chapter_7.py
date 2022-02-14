# converting a vedio into Gray and Black and white
# import a library 
import cv2 as cv
# load a video into the veriable which name is designted as cap
cap = cv.VideoCapture('resourses/video.mkv')
# add a while loop to read a video
while (True):   # condition applied of while loop
    (ret,frame) =  cap.read()   # read the video and convert into the frame
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)    #convert the video ito graycolor
    (thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)   #convert he video into the black
    # To Show in Player on the screen
    if ret == True:
        cv.imshow("vedio",binaryimg)    # after conversion Binary video will displayed
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):    # q press and screen will be quit
            break
    else:
        break 

# after the dispaly of video the cap will release the events which has been generated
cap.release()
# close all the windows which were running.
cv.destroyAllWindows()