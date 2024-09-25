import cv2
import numpy as np

def otsu_segment_image(image_path):
    # Step 1: Load the image in grayscale
    image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)  
    # cv2.imread(image_path, cv2.IMREAD_GRAYSCALE): reads the image in grayscale

    # Step 2: Apply Otsu's thresholding
    _, segmented_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.threshold() with cv2.THRESH_OTSU automatically determines the optimal threshold value
    # - The function returns the threshold used (we ignore it by using `_`) and the binary image
    # - The 0 here is a placeholder for the threshold value since Otsu's method calculates it automatically

    # Step 3: Return the segmented image
    return segmented_image  # Return the segmented image after applying Otsu's thresholding

# Example usage
segmented_image = otsu_segment_image('montage.png')  # Apply Otsu's threshold segmentation

# Display the result
cv2.imshow("Segmented Image", segmented_image)  # Show the segmented image
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows after key press
