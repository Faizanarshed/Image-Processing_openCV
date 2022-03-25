# import the libraries 
# into the file like open cv and numpy
import numpy as np
import cv2 as cv
# make a veriable 
# store the data into the veriable using the attributes
img = cv.imread('resourses/img1.jpeg')
# resize the size of the image 
img1 = cv.resize(img,(100,100))
# display the image on screen
# original image 
cv.imshow("Pahli Image",img)
# after implement the resize function display the updated image
cv.imshow("Dusri image",img1)
# create a veriable and store the gray image.
# BGR function applied on the image
gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# show the gray image on the screen
cv.imshow("Gray",gray)
# image hold
cv.waitKey(0)
cv.destroyAllWindows()