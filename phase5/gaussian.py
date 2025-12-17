import cv2

image = cv2.imread('doctor_resized.png', 1)
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    gaussian_image = cv2.GaussianBlur(image, (15, 15), 0)
    # Apply Gaussian blur with a 15x15 kernel and standard deviation of 0
    cv2.imwrite('gaussian_blurred_image.png', gaussian_image)
    cv2.imshow('Gaussian Blurred Image', gaussian_image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()