import cv2
cap = cv2.VideoCapture(2)  # 0 is usually the default camera
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    print("Video capture started successfully.")
    while True:
        ret, frame = cap.read() 
        # ret is a boolean indicating if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break
        cv2.imshow('Video Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()