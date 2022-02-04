import numpy as np
import cv2 as cv


img = cv.imgread('resourses/img1.jpg')


img = cv.resize(800,600)


cv.imshow("Original",img)
cv.imshow("Original",img)

gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


cv.waitKey(0)

cv.destroyAllWindows()