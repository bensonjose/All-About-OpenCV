import numpy as np
import cv2

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Get the width and height of the frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Convert the frame from BGR color space to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper HSV bounds for detecting blue color
    lower_blue = np.array([110, 50, 50])  # Lower bound for blue color
    upper_blue = np.array([130, 255, 255])  # Upper bound for blue color

    # Create a mask that filters out only the blue color within the specified HSV range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply the mask to the original frame to highlight the blue color
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame with the blue color highlighted
    cv2.imshow('frame', result)

    # Display the mask that isolates the blue color
    cv2.imshow('mask', mask)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
