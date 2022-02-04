import numpy as np
import cv2 as cv
img = cv.imgread('')
img = cv.resize(800,600)
cv.imshow("Original",img)

cv.waitKey(0)
cv.destroyAllWindows()