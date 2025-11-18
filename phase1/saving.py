import cv2
# 0,1,-1 are flags for reading images in different modes
image = cv2.imread('virujlogo.png',1) 
cv2.imwrite('virujlogo_copy.png', image)

# 0 indicates grayscale
# 1 indicates color
# -1 indicates unchanged (including alpha channel if present)