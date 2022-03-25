import cv2 as cv
from cv2 import imwrite

cap = cv.VideoCapture(0)

frameNr = 0

while(True):
    success,frame =cap.read()
    if success:
        cv.imwrite(f"resourses/frame/frame_{frameNr}.jpg", frame)
    else:
        break
    framesNr = framesNr + 1

cap.release()

