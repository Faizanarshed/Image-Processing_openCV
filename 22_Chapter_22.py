#import libraries
# open cv and numpy
import cv2 as cv
import numpy as np
# make a veriable in which import a cascadeclassifier
# load a file from resourses database
face_cascade = cv.CascadeClassifier("resourses/haarcascade_frontalface_default.xml")
# make an image and import the data in the form of image
# load the data set in the veriable
img = cv.imread("resourses/image1.jpg")
# make a veriable which stored the fray image
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 
faces = face_cascade.detectMultiScale(gray_img,1.1,4)
#draw a rectangle on the image to detect the face
# use for loop 
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# check the size of the image 
print(img.shape)
#show the image on the scale 
cv.imshow("image",img)
# store the image into the resourses folder
cv.imwrite("resourses/faces.jpg",img)
# Display the image and wait it umtill the q press
cv.waitKey(0)
# destroy all windows
cv.destroyAllWindows()