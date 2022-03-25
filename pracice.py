import cv2
 
 
def on_change(val):
 
    imageCopy = img.copy()
 
    cv2.putText(imageCopy, str(val), (0, imageCopy.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 4)
    cv2.imshow(windowName, imageCopy)
 
 
img = cv2.imread('resourses/img2.jpeg')
 
windowName = 'image'
 
cv2.imshow(windowName, img)
cv2.createTrackbar('slider', windowName, 0, 100, on_change)
 
cv2.waitKey(0)
cv2.destroyAllWindows()