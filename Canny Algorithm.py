import cv2
image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 100, 200)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
