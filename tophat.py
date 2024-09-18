import cv2
import numpy as np
image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('Top-Hat', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
