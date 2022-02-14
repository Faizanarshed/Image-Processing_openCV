import cv2 as cv
import numpy as np


face_cascade = cv.CascadeClassifier("resourses/haarcascade_frontalface_default.xml")

img = cv.imread("resourses/image1.jpg")

gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,1.1,4)
#draw a rectangle
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


print(img.shape)





cv.imshow("image",img)
cv.imwrite("resourses/faces.jpg",img)
cv.waitKey(0)
cv.destroyAllWindows()