import numpy as np
import cv2

# Opening the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Loading Haar cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    # Reading a frame from the camera
    ret, frame = cap.read()

    # Converting the frame to grayscale for face and eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting faces in the grayscale frame using the face cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Loop through the detected faces
    for (x, y, w, h) in faces:
        # Drawing a rectangle around each detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        # Region of Interest (ROI) for the detected face in grayscale and color
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detecting eyes within the ROI of the face
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5)

        # Loop through the detected eyes within the face ROI
        for (ex, ey, ew, eh) in eyes:
            # Drawing a rectangle around each detected eye within the face
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    # Displaying the frame with rectangles drawn around detected faces and eyes
    cv2.imshow('frame', frame)

    # Checking for a key press, and if 'q' is pressed, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Releasing the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
