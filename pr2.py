
import cv2 as cv


def slider():
    pass
path = "resourses/image1.jpeg"
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 1020, 400)
cv.createTrackbar("Hue Min", "Bars" , 0 ,255 , slider)
cv.waitKey(0)
cv.destroyAllWindows()