import cv2

image = cv2.imread('doctor_resized.png', 1)

if image is not None:
    (h, w,c) = image.shape
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, 45, 1.0) 
    # Rotate the image by 45 degrees around its center with a scale of 1.0
    # 1.0 means no scaling
    # 0.5 would mean reducing the size by half
    # 2.0 would mean doubling the size
    rotated_image = cv2.warpAffine(image, M, (w, h))
    # warpAffine applies the rotation matrix M to the image
else:
    print("Error: Image not found or unable to load.")

cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
