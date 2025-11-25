import cv2
image = cv2.imread('doctor.png', 1)

image_resized = cv2.resize(image, (200, 200), interpolation=cv2.INTER_AREA)
cv2.imwrite('doctor_resized.png', image_resized)

