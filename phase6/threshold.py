import cv2
import numpy as np
image = cv2.imread('doctor_resized.png', 1)

ret, thresholded_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
# Apply binary thresholding with a threshold value of 127
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    cv2.imwrite('thresholded_image.png', thresholded_image)
    cv2.imshow('Thresholded Image', thresholded_image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()