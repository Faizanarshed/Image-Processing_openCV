# Title of the File 
#   Convert an Image into Black and White
#   import the libraries
import cv2 as cv
from cv2 import cvtColor
#   original image which load into the veriable
img = cv.imread("resourses/img2.jpeg")
#   original image convert into the gray image
gray = cvtColor(img, cv.COLOR_BGR2GRAY)
#   gray image convert into the  binary image 
(thresh,binaryimg) = cv.threshold(gray,127,255,cv.THRESH_BINARY)
#   Displaay Image into different images
#   Display binary Image into Binary Image
cv.imshow('Black and White Image',binaryimg)
#   Display the Gray Image on the Screen
cv.imshow('Gray image',gray)
#   Display the Original Image on the Screen
cv.imshow('original',img)
#   Delay window
cv.waitKey(0)
cv.destroyAllWindows()