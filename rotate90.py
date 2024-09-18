import cv2 
import numpy as np
def rotate_image(image,angle):
    (h,w) = image.shape[:2]
    center =(w//2,h//2)
    rotation_matrix=cv2.getRotationMatrix2D(center,angle,1.0)
    rotated_image=cv2.warpAffine(image,rotation_matrix,(w,h))
    return rotated_image
img = cv2.imread("montage.png")
rotated_90 = rotate_image(img,-90)
cv2.imshow("Orginial Image",img)
cv2.imshow("Rotated 90 degrees",rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()


