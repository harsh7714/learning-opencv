import cv2

cap = cv2.VideoCapture(0)  # 0 is usually the default camera

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', codec, fps, (frame_width, frame_height))
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
        out.write(frame)  # Save the frame to the output file
        cv2.imshow('Video Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Press 'q' to exit the video window  
        # 0xFF is used to get the last 8 bits of the keycode  
    cap.release()
    cv2.destroyAllWindows()