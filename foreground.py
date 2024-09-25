import cv2
import numpy as np

def subtract_foreground(image_path, lower_bound, upper_bound):
    # Step 1: Read the image from the file path
    image = cv2.imread("smiles.jpeg")  # cv2.imread() loads an image from a file

    # Step 2: Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # cv2.cvtColor() converts image from one color space to another

    # Step 3: Create a mask for the foreground color range (what to subtract)
    mask = cv2.inRange(hsv, np.array(lower_bound), np.array(upper_bound))  
    # cv2.inRange() creates a binary mask where the colors within the specified bounds are set to white

    # Step 4: Use the mask to keep only the background
    background = cv2.bitwise_and(image, image, mask=mask)  
    # cv2.bitwise_and() applies the mask and keeps the part of the image where the mask is white

    # Step 5: Return or display the background
    return background  # Return the processed image

# Example usage:
lower_bound = [30, 50, 50]  # Adjust based on the foreground color
upper_bound = [85, 255, 255]
background = subtract_foreground('smiles.jpeg', lower_bound, upper_bound)

# Display the result
cv2.imshow("Background", background)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
