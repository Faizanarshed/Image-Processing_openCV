#coordinates of an image or video


# Step 1 import library


import cv2 as cv
import numpy as np

# Step 2 define a function

def find_cord(event,x ,y, flag,params):
    if event ==cv.EVENT_LBUTTONDOWN:


        #left mouse click
        print(x,'',y)

        #how to define or print the sa,e image or vedio
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x)+ ','  +str(y),(x,y),font,1,(255,0,0),thickness=2)

        #Show the text on the image and img itself
        cv.imshow('image',img)
    #for color find of the selected area
    if event==cv.EVENT_RBUTTONDOWN:
        print(x,',',y)

        font = cv.FONT_HERSHEY_SIMPLEX
        b = [y,x,0]
        g = [y,x,1]
        r = [y,x,2]

        cv.putText(img,str(b)+','+str(g),','+str(r),(x,y),font,1,(255,0,0),2)
        cv.IMWRITE_PNG_STRATEGY_DEFAULT('image',img)


# final function to read an display
if __name__=="__main__":
    #reading an image
    img = cv.imread('resourses/img1.jpeg')
    #Dispalyy the image
    cv.imshow('image',img)
    cv.setMouseCallback("image",find_cord)
    cv.waitKey(0)
    cv.destroyAllWindows()


