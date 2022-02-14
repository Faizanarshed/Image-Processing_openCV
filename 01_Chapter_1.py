
# import the libraries
# open cv library which will use inthe entire course
import cv2 as cv
# import the dataset into and store it to the veriable
img = cv.imread('resourses/img1.jpeg')
# imshow use to disply the image on the screen
cv.imshow("Original",img)
# waitkey use to display the image untill no quit
cv.waitKey(0)
# destroy all windows
cv.destroyAllWindows()