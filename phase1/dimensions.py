import cv2
image = cv2.imread('virujlogo.png',1)

if image is not None:
    h,w,c= image.shape
    print(f"Height: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Error: Image not found or unable to load.")    