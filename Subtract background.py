import cv2
import numpy as np

def subtract_background(image_path, lower_bound, upper_bound):
    # Step 1: Read the image from the file path
    image = cv2.imread("smiles.jpeg")  # cv2.imread() loads an image from a file

    # Step 2: Convert the image from BGR (OpenCV default) to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # cv2.cvtColor() converts image from one color space to another

    # Step 3: Create a mask where the background color range is defined by lower and upper bounds
    mask = cv2.inRange(hsv, np.array(lower_bound), np.array(upper_bound))  
    # cv2.inRange() creates a binary mask where the colors within the specified bounds are set to white, and others to black

    # Step 4: Invert the mask to get the opposite region (foreground)
    mask_inv = cv2.bitwise_not(mask)  # cv2.bitwise_not() inverts a binary mask (i.e., black becomes white, white becomes black)

    # Step 5: Apply the mask to the original image, keeping only the foreground
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)  
    # cv2.bitwise_and() applies the mask and keeps the part of the image where the mask is white

    # Step 6: Return or display the foreground (without the background)
    return foreground  # Return the processed image

# Example usage:
lower_bound = [0, 0, 0]  # Adjust based on the background color
upper_bound = [179, 255, 50]
foreground = subtract_background('smiles.jpeg', lower_bound, upper_bound)

# Display the result using OpenCV's imshow() function
cv2.imshow("Foreground", foreground)
cv2.waitKey(0)  # Waits for a key press to close the window
cv2.destroyAllWindows()  # Closes all OpenCV windows
