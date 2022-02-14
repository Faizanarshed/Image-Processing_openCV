#import libraries
import cv2 as cv
from cv2 import cvtColor
# load image into the veriable 
img = cv.imread('resourses/img1.jpeg')
#resize the image
img1 = cv.resize(img,(100,100))
#   img1 = cv.resize(img,(800,600))
#   make a veriable and store a grey image into the veriable
gray_img = cvtColor(img,cv.COLOR_BGR2GRAY)
#   displaycode
#   Display the original image 
cv.imshow("Pahli image",img)
# Display the Gray image on the Display
cv.imshow("Gray Image",gray_img)
#Gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",gray)
#delaycode
# wait Key and destroy all the Windows
cv.waitKey(0)
cv.destroyAllWindows()