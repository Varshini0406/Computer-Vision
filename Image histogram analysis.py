import cv2 
import matplotlib.pyplot as plt
def plot_histogram(image):
    colors=("b","g","r")
    channels = cv2.split(image)
    plt.figure()
    plt.title("Histogram of Image Channels")
    for i,(ch,color) in enumerate(zip(channels,colors)):
        plt.hist(ch.ravel(),bins=256,color=color,label=f"Channel{i+1}")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Number of Pixels")
        plt.legend()
        plt.show()
img = cv2.imread("montage.png")
plot_histogram(img)

