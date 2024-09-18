import cv2
import numpy as np
image = cv2.imread('montage.png')
x1, y1 = 100, 100   
x2, y2 = 300, 300 
roi = image[y1:y2, x1:x2]
new_img = np.zeros_like(roi)
new_img[:] = roi
cv2.imshow('Image with ROI Pasted', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('image_with_roi_pasted.jpg', new_img)
