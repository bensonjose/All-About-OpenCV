import numpy as np
import cv2

# Load the input image
img = cv2.imread(r"C:\Users\Bindu\OpenCV Prac\Roundup-White-Houses-11-A-A-House-DVA-Arhitekta-600x600.jpg")

# Display the original image
cv2.imshow('Initial Frame', img)

# Resize the image to 75% of its original size
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# Convert the resized image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform corner detection using the Shi-Tomasi method
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert the detected corner coordinates to integers
corners = np.int0(corners)

# Loop through each detected corner and draw a circle around it
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# Loop through all pairs of detected corners and draw lines between them
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

# Display the final image with corners and lines
cv2.imshow('Frame', img)

# Wait for a key press and close the windows when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
