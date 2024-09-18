import cv2
import numpy as np
image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.sqrt(cv2.addWeighted(cv2.pow(sobelx, 2), 0.5, cv2.pow(sobely, 2), 0.5, 0))
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
