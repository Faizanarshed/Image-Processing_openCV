# Basic Functions in open cv
# import the libraries
import cv2 as cv
import numpy as np
# import or add two images for comparison
img1 = cv.imread("resourses/img1.jpeg")  # 1st image 
img = cv.imread("resourses/image1.jpg") # 2nd image
#resize img
# call a veriable and resize the original image and store it into the new veriable
resize_img = cv.resize(img,(53,53))
# Gray Img
# call a new veriable put the function on the original image and store it into the veriable
Gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blures Image 
# call the new veriable and store new values in it
blurr_img = cv.GaussianBlur(img, (3,3),0)
# Black_White Image
# store the new binary images properties into the new veriable 
(thresh,binaryimg) = cv.threshold(Gray_img,127,255,cv.THRESH_BINARY)
# edge detection
edge_img = cv.Canny(img, 48,48)
#thikness of lines
mat_kernel = np.ones((3,3), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel),iterations=1)
# make a Thinner OutLine
ero_img = cv.erode(dilated_img,mat_kernel,iterations=1)
# Cropping Image we use numpy library not open cv
print("the size of the image is: ",img.shape)
cropped_img = img[0:500,150:400]
# show image on the display
cv.imshow('original_image', img)# line of code will display the original image on the screen
cv.imshow('ReShape_image', resize_img) # this line of code will display the resized image on the screen
cv.imshow('Gray_image', Gray_img) # code show us he gray image which is stored on the gray_img veriable
cv.imshow('Blur_image', blurr_img) #blurred image will display on the screen
cv.imshow('Edge', edge_img) # image with edges will display
cv.imshow('Dilated_image', dilated_img) # dilated_img willl be on the screen
cv.imshow('mat_kernal',mat_kernel)  # impliment the mat_kernel properties on the image 
cv.imshow('Ero_image',ero_img)  #ero_img will display on the screen
cv.imshow('Black_White Image',binaryimg) # the line will show us the binary image on the screen
cv.imshow("cropped_img",cropped_img) #cropped image will be displayed on the screen
cv.waitKey(0)   # wait key
cv.destroyAllWindows()  # close all the windows