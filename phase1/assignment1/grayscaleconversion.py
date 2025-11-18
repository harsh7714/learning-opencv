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

image = cv2.imread(path, 0)  # Read the image in grayscale mode

print("Select:\n1:Display Image\n2:Save Image")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
    if image is None:
        print("Error: Image not found or unable to load.")
    else:
        cv2.imshow('Grayscale Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
elif choice == '2':
    if image is None:
        print("Error: Image not found or unable to load.")
    else:
        save_path = 'grayscale_image.png'
        cv2.imwrite(save_path, image)
        print(f"Image saved successfully at {save_path}")
else:
    print("Invalid choice. Please enter 1 or 2.")   