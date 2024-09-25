import cv2  # Import OpenCV library
import numpy as np  # Import NumPy for handling arrays (optional for some operations)

def segment_image(image_path, threshold_value, max_value=255):
    # Step 1: Load the image in grayscale (so we work with pixel intensities)
    image = cv2.imread("montage.png", cv2.IMREAD_GRAYSCALE)  
    # cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) reads the image in grayscale mode.

    # Step 2: Apply simple thresholding
    _, segmented_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)  
    # cv2.threshold() applies a simple threshold:
    # - image: the input image
    # - threshold_value: pixel intensity above this value will be set to max_value
    # - max_value: the value to assign to pixels exceeding the threshold
    # - cv2.THRESH_BINARY: binary thresholding mode (i.e., only two values: 0 or max_value)
    # The function returns a tuple: (threshold used, the resulting binary image). 
    # Since we don't need the threshold used, we use `_` to ignore the first returned value.

    # Step 3: Return the segmented image
    return segmented_image  # Return the binary image after thresholding

# Example usage
threshold_value = 128  # Define a threshold value (adjust based on your image)
segmented_image = segment_image('montage.png', threshold_value)  # Segment the image

# Display the result
cv2.imshow("Segmented Image", segmented_image)  # cv2.imshow() displays the image in a window
cv2.waitKey(0)  # Waits for a key press (0 means wait indefinitely)
cv2.destroyAllWindows()  # Closes all OpenCV windows after the key press
