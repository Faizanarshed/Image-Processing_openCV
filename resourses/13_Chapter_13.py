#basic functions or manuplation in open cv
import cv2 as cv
# import or add a picure
img = cv.imread("resourses/img1.jpeg")

#resize img
resize_img = cv.resize(img,(460,450))
# Gray Img
Gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blures Image 

blurr_img = cv.GaussianBlur(img, (7,7),0)

# edge detection
edge_img = cv.Canny(img, 48,48)

#thikness of lines
dilated_img = cv.dilate(edge_img,(7,7),iterations=1)


cv.imshow('original_image', img)
#cv.imshow('ReShape_image', resize_img)
#cv.imshow('Gray_image', Gray_img)
#cv.imshow('Blur_image', blurr_img)
cv.imshow('Edge', edge_img)
cv.imshow('Dilated_image', dilated_img)
#cv.imshow("frame",frame)
cv.waitKey(0)
cv.destroyAllWindows()