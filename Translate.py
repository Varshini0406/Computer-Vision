import cv2
import numpy as np

def translate_image(image, x_shift, y_shift):
  (h, w) = image.shape[:2]
  translation_matrix = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
  translated_image = cv2.warpAffine(image, translation_matrix, (w, h))
  return translated_image
img = cv2.imread("montage.png")
translated_img = translate_image(img, 50, 100)
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
