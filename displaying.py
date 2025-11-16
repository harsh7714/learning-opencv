import cv2

image = cv2.imread('virujlogo.png',0) 

if image is None:
    print("Error: Image not found or unable to load.")
else:
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()