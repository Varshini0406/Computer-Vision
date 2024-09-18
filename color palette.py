import cv2
import numpy as np

def on_trackbar(val):
  global img, blue, green, red
  blue = cv2.getTrackbarPos("Blue", "Color Palette")
  green = cv2.getTrackbarPos("Green", "Color Palette")
  red = cv2.getTrackbarPos("Red", "Color Palette")
  img[:] = [blue, green, red]
  cv2.imshow("Color Palette", img)

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Create a window and trackbars
cv2.namedWindow("Color Palette")
cv2.createTrackbar("Blue", "Color Palette", 0, 255, on_trackbar)
cv2.createTrackbar("Green", "Color Palette", 0, 255, on_trackbar)
cv2.createTrackbar("Red", "Color Palette", 0, 255, on_trackbar)

# Show the window
on_trackbar(0)
cv2.imshow("Color Palette", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
