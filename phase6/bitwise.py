import cv2
import numpy as np

img1 = np.zeros((300, 300, 3), dtype=np.uint8)
img1 = cv2.rectangle(img1, (50, 50), (250, 250), (255, 255, 255), -1)
# Create a white square on a black background
img2 = np.zeros((300, 300, 3), dtype=np.uint8)
img2 = cv2.circle(img2, (150, 150), 100, (255, 255, 255), -1)
# Create a white circle on a black background   
if img1 is None or img2 is None:
    print("Error: Could not create images.")
else:
    print("Images created successfully.")
    bitwise_and = cv2.bitwise_and(img1, img2)
    bitwise_or = cv2.bitwise_or(img1, img2)
    bitwise_xor = cv2.bitwise_xor(img1, img2)
    bitwise_not_img1 = cv2.bitwise_not(img1)
    bitwise_not_img2 = cv2.bitwise_not(img2)

    cv2.imshow('Image 1 - Square', img1)
    cv2.imshow('Image 2 - Circle', img2)
    cv2.imshow('Bitwise AND', bitwise_and)
    cv2.imshow('Bitwise OR', bitwise_or)
    cv2.imshow('Bitwise XOR', bitwise_xor)
    cv2.imshow('Bitwise NOT Image 1', bitwise_not_img1)
    cv2.imshow('Bitwise NOT Image 2', bitwise_not_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()