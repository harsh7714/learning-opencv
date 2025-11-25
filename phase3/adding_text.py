import cv2
image = cv2.imread('doctor_resized.png', 1) 
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    cv2.putText(image, 
                'Hello, OpenCV!',  # Text to be added
                (50, 50),          # Bottom-left corner of the text string in the image
                cv2.FONT_HERSHEY_SIMPLEX,  # Font type
                0.1,                 # Font scale (size)
                (0, 0, 255),      # Text color in BGR (Red)
                2,                 # Thickness of the text
                cv2.LINE_AA)      # Line type (anti-aliased)
    # putText adds the specified text to the image at the given position with the defined font
    cv2.imshow('Text Image', image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     