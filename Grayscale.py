import cv2
import numpy as np
img = cv2.imread("montage.png")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image', img)
cv2.imshow('Gray image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
