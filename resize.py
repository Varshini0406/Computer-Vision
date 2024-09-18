import cv2
import numpy as np
img = cv2.imread("montage.png")
enlarge = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2))
shrunken = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Original image",img)
cv2.imshow("Enlargered image",enlarge)
cv2.imshow("Shrunken image",shrunken)
cv2.waitKey(0)
cv2.destroyAllWindows()
