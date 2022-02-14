# Acivate the Webcam through Python code
#   Activate the Open CV Function

# import the Libraries
import cv2 as cv


# load a video into the code
# call the webcame into the veriable (cap)
cap = cv.VideoCapture(0)


# writing format ,codec,video writer object and file output
#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
#out = cv.VideoWriter('resourses/out_vedio.avi',cv.VideoWriter_fourcc('M',"j",'P','G'),10,(frame_width,frame_height))

while (True):
    (ret,frame) =  cap.read()   # read the video and convert into the frame
    #grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)   #convert the video ito graycolor
    #(thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)#convert he video into the black
    # To Show in Player
    if ret == True:
        #out.write(grayframe)
        #cv.imshow("vedio",grayframe)   # this line of code will display the cam video after convert it into the Gray image
        cv.imshow("vedio",frame)        # this line of code will display the original cam video 
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):    # to quit the video from the screen this line of code will use
            break
    else:
        break 
# release all the values store in the cap veriable
cap.release()
# destroy all the windows
cv.destroyAllWindows()