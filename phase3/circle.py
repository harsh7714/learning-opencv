import cv2 
image = cv2.imread('doctor_resized.png', 1) 
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    center = (image.shape[1] // 2, image.shape[0] // 2)  # Calculate the center of the image
    radius = 100  # Define the radius of the circle
    circle_image = cv2.circle(image, center, radius, (255, 0, 0), 3) 
    # Draw a blue circle at the center of the image with a radius of 100 pixels and a thickness of 3 pixels      
    cv2.imshow('Circle Image', circle_image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()