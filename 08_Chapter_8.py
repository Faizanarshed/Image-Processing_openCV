# converting a vedio into Gray and Black and white

#import a library 
import cv2 as cv
# load a video into the code
cap = cv.VideoCapture('resourses/video.mkv')
# writing format ,codec,video writer object and file output
frame_width = int(cap.get(3))   # adjust the size of the vedio frame in width
frame_height = int(cap.get(4))  # adjust the size of the vedio frame in height
# call a veriable out
# store the video in the particular format in the veriable
# in this line of code 10 is defined as number of frames 
out = cv.VideoWriter('resourses/out_vedio.avi',cv.VideoWriter_fourcc('M',"J",'P','G'),10,(frame_width,frame_height),isColor= False)
# use the while Loop to display the video
while (True):
    (ret,frame) =  cap.read()# read the video and convert into the frame
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#convert the video ito graycolor
    #(thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)#convert he video into the black
    # To Show in Player
    if ret == True:
        out.write(grayframe)    # video convert into the frames 
        cv.imshow("vedio",grayframe)    # video display on the screen
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):    # To Quit the Video from the screen
            break
    else:
        break 

cap.release()   # cap veriable will release the data
out.release()   # out veriable will release the video data 
cv.destroyAllWindows() # cv attributes to kill all the windows