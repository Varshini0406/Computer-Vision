import cv2
import numpy as np

def adaptive_segment_image(image_path, max_value=255, block_size=11, C=2):
    # Step 1: Load the image in grayscale mode
    image = cv2.imread('montage.png', cv2.IMREAD_GRAYSCALE)  
    # cv2.imread(image_path, cv2.IMREAD_GRAYSCALE): reads the image in grayscale

    # Step 2: Apply adaptive thresholding
    segmented_image = cv2.adaptiveThreshold(
        image, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)
    # cv2.adaptiveThreshold() works as:
    # - image: the input grayscale image
    # - max_value: the value to assign to pixels exceeding the locally computed threshold
    # - cv2.ADAPTIVE_THRESH_GAUSSIAN_C: adaptive method that uses the weighted mean of neighboring pixels
    # - cv2.THRESH_BINARY: binary thresholding mode
    # - block_size: size of the pixel neighborhood to compute the threshold (must be an odd number)
    # - C: constant subtracted from the mean or weighted mean in the adaptive thresholding process

    # Step 3: Return the segmented image
    return segmented_image  # Return the binary image after adaptive thresholding

# Example usage
segmented_image = adaptive_segment_image('montage.png')  # Apply adaptive threshold segmentation

# Display the result
cv2.imshow("Segmented Image", segmented_image)  # Show the segmented image
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows after key press
