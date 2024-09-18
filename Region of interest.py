import cv2
import numpy as np

def process_roi(image, roi_x, roi_y, roi_width, roi_height):
  roi = image[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
  processed_roi = cv2.blur(roi, (5, 5))  
  image[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width] = processed_roi
  return image
img = cv2.imread("montage.png")
roi_x, roi_y, roi_width, roi_height = 100, 200, 150, 100
processed_img = process_roi(img, roi_x, roi_y, roi_width, roi_height)
cv2.imshow("Original Image", img)
cv2.imshow("Processed Image", processed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
