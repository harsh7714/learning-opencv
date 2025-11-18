import cv2

image = cv2.imread('doctor.png') 

if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")