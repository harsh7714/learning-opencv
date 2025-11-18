import cv2

image = cv2.imread('doctor.png', 1)

if image is not None:
    cropped_image = image[50:250, 100:300]
else:
    print("Error: Image not found or unable to load.")

cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()