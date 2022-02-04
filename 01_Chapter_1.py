
import cv2 as cv


img = cv.imread('resourses/img1.jpeg')

cv.imshow("Original",img)

cv.waitKey(0)

cv.destroyAllWindows()