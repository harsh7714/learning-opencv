import cv2

image = cv2.imread('gaussian_blurred_image.png', 1)
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    median_blurred_image = cv2.medianBlur(image, 15)
    # Apply Median blur with a kernel size of 15
    cv2.imwrite('median_blurred_image.png', median_blurred_image)
    cv2.imshow('Median Blurred Image', median_blurred_image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()