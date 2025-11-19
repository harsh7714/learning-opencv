import cv2
image = cv2.imread('doctor_resized.png', 1) 
if image is not None:
    flipped_image = cv2.flip(image, -1) 
    # Flip the image horizontally
    # 0 would flip vertically
    # 1 would flip horizontally
    # -1 would flip both vertically and horizontally
else:
    print("Error: Image not found or unable to load.")      
cv2.imshow('Flipped Image', flipped_image)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()     