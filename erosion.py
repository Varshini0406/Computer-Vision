import cv2
import numpy as np
def apply_erosion(image, kernel_size, iterations):
  kernel = np.ones(kernel_size, np.uint8)
  eroded_image = cv2.erode(image, kernel, iterations=iterations)
  return eroded_image
img = cv2.imread("montage.png")
eroded_img = apply_erosion(img, (3, 3), 2)
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
