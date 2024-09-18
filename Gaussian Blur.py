import cv2
import numpy as np
img = cv2.imread("montage.png")
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("Original image",img)
cv2.imshow("Blurred image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
