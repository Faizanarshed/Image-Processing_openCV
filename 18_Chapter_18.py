# how to change a prospective of an image


import cv2 as cv
import numpy as np

img = cv.imread("resourses/img1.jpeg")
print(img.shape)

height = 900
weidth = 800

height,weidth = 900,800
# Defineing a point


point1 =  np.float32([[233,196],[82,471],[522,169],[715,482]])




#np.matrix = cv.getPerspectiveTransform()





