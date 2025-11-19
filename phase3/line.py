import cv2
image = cv2.imread('doctor_resized.png', 1) 
if image is not None:
    imageline = cv2.line(image, (0, 0), (150, 150), (255, 0, 0), 5) 
    # Draw a blue line from the top-left corner (0,0) to the point (150,150) with a thickness of 5 pixels
else:
    print("Error: Image not found or unable to load.")      
cv2.imshow('Line Image', imageline)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()