import cv2
image = cv2.imread('doctor.png', 1)

image_resized = cv2.resize(image, (200, 200), interpolation=cv2.INTER_AREA)
cv2.imwrite('doctor_resized.png', image_resized)

img = cv2.imread('doctor_resized.png', 1)
if img is not None:
    h, w, c = img.shape
    print(f"Height: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Error: Image not found or unable to load.")