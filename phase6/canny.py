import cv2
import numpy as np
image = cv2.imread('doctor_resized.png', 1)
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert the image to grayscale
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 1.4)
    # Apply Gaussian blur with a 5x5 kernel and standard deviation of 1.4
    canny_edges = cv2.Canny(blurred_image, 100, 200)
    # Apply Canny edge detection with thresholds 100 and 200
    cv2.imwrite('canny_edges_image.png', canny_edges)
    cv2.imshow('Canny Edges Image', canny_edges)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()