import cv2
image = cv2.imread('doctor_resized.png', 1) 
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    pt1 = (50, 50)  # Top-left corner of the rectangle
    pt2 = (200, 150)  # Bottom-right corner of the rectangle
    rectangle_image = cv2.rectangle(image, pt1, pt2, (0, 255, 0), 3) 
    # Draw a green rectangle with top-left corner at (50,50) and bottom-right corner at (200,150) with a thickness of 3 pixels      
    cv2.imshow('Rectangle Image', rectangle_image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    