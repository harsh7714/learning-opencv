import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the main Tkinter window
Tk().withdraw()

# Open file dialog
path = askopenfilename(
    title="Select an image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

print("Selected:", path)

# Load with OpenCV
img = cv2.imread(path)

if img is None:
    print("Failed to load image.")
else:
    cv2.imshow("Selected Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
