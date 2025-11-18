import cv2

image = cv2.imread('doctor_resized.png', 1)

if image is not None:
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
else:
    print("Error: Image not found or unable to load.")

cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
