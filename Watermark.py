import cv2
source_image = cv2.imread('montage.png')
text = "Watermark"
position = (source_image.shape[1] - 100, source_image.shape[0] - 50)
cv2.putText(source_image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
cv2.imshow('Text Watermarked Image', source_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('text_watermarked_image.jpg', source_image)
