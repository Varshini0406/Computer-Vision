import cv2
import numpy as np
image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('Black-Hat', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
