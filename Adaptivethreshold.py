import cv2
image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)
adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Adaptive Mean', adaptive_mean)
cv2.imshow('Adaptive Gaussian', adaptive_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
