import numpy as np
import cv2 as cv
from cv2 import cvtColor


img = cv.imgread('resourses/img1.jpg')


img1 = cv.resize(800,600)

#conversion
gray_img = cvtColor(img,cv.COLOR_BGRGRAY)
#displaycode
cv.imshow("Pahli image",img)
cv.imshow("Gray Image",gray_img)

gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


cv.waitKey(0)

cv.destroyAllWindows()