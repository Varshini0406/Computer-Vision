import cv2
import numpy as np

def find_contours(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  return contours
img = cv2.imread("montage.png")
contours = find_contours(img)
for cnt in contours:
  cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2)
for cnt in contours:
  for pt in cnt:
    print(pt)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

