import cv2 as cv
import numpy as np


fsce_cascade = cv.CascadeClassifier()

img = cv.imread("resourses/img2.jpeg")

print(img.shape)





cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()