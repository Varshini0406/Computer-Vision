import cv2
import numpy as np

def apply_smoothing(image, kernel_size):
  kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])
  smoothed_image = cv2.filter2D(image, -1, kernel)
  return smoothed_image
img = cv2.imread("montage.png")
smoothed_img = apply_smoothing(img, (5, 5))
cv2.imshow("Original Image", img)
cv2.imshow("Smoothed Image", smoothed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
