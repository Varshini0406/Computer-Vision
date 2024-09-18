import cv2
import numpy as np
image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)
prewittx=cv2.Sobel(image,cv2.CV_32F,1,0,ksize=3)
prewitty=cv2.Sobel(image,cv2.CV_32F,0,1,ksize=3)
prewittx_8u=cv2.convertScaleAbs(prewittx)
prewitty_8u=cv2.convertScaleAbs(prewitty)
prewitt_combined = cv2.addWeighted(prewittx_8u, 0.5, prewitty_8u, 0.5, 0)
cv2.imshow('Prewitt X', prewittx)
cv2.imshow('Prewitt Y', prewitty)
cv2.imshow('Prewitt Combined', prewitt_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
