# how to detect specific color 

import numpy as np
import cv2 as cv
from cv2 import imshow
img = cv.imread('resourses/image1.jpeg')
# convert in hsv(Hue,Saturation,Value)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#   sliders
def slider():
    pass
path = "resourses/image1.jpeg"
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 900, 300)
cv.createTrackbar("Hue Min", " Bars ", 0,179,slider)
cv.createTrackbar("Hue Max", " Bars ", 179,179,slider)
cv.createTrackbar("Sat Min", " Bars ", 0,255,slider)
cv.createTrackbar("Sat Max", " Bars ", 255,255,slider)
cv.createTrackbar("Val Min", " Bars ", 0,255,slider)
cv.createTrackbar("Val Max", " Bars ", 255,255,slider)

img = cv.imread(path)
hue_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
while True:
    img = cv.imread(path)
    hue_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min= cv.getTrackbarPos("Hue Min","Bars")
    Hue_max = cv.getTrackbarPos("Hue Max","Bars")
    sat_min = cv.getTrackbarPos("Sat Min","Bars")
    sat_max = cv.getTrackbarPos("Sat Max","Bars")
    val_min = cv.getTrackbarPos("Val Min","Bars")
    val_max = cv.getTrackbarPos("Val Max","Bars")
    print(hue_min,Hue_max,sat_min,sat_max,val_min,val_max)


    cv.imshow("original", img) 
    cv.imshow('Hue',hue_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break








    
