import cv2
import numpy as np
image = cv2.imread('doctor_resized.png', 1) 
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    # Create a sharpening kernel
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1,  5, -1],
                                  [0, -1, 0]])
    # Apply the sharpening filter to the image
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    cv2.imwrite('sharpened_image.png', sharpened_image)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()