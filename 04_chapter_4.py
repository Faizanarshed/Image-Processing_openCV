# conver an image into Black and White
import cv2 as cv
from cv2 import cvtColor

img = cv.imread("resourses/img.jpg")

gray = cvtColor(img, cv.COLOR_BGR2GRAY)
gray

#(thresh,b_w) = cv.