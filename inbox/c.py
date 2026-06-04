import cv2
import numpy as np
def main():
    # Load the image
    image = cv2.imread('input.jpg')
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    # Save the result
    cv2.imwrite('edges.jpg', edges)
    