import numpy as np
import cv2

# Load and resize the main imagesc
img = cv2.resize(cv2.imread(r"C:\Users\Bindu\OpenCV Prac\dani-1579850874.jpg", 0), (0, 0), fx=0.8, fy=0.8)

# Load and resize the template image
template = cv2.resize(cv2.imread(r"C:\Users\Bindu\Downloads\dani-1579850874.jpg", 0), (0, 0), fx=0.8, fy=0.8)

# Get the height and width of the template image
h, w = template.shape

# List of template matching methods to try
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Iterate through each template matching method
for method in methods:
    img2 = img.copy()

    # Apply template matching using the current method
    result = cv2.matchTemplate(img2, template, method)

    # Find the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Depending on the method, set the location accordingly
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # Calculate the coordinates of the bottom-right corner of the detected region
    bottom_right = (location[0] + w, location[1] + h)

    # Draw a rectangle around the detected region
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    # Display the image with the rectangle
    cv2.imshow('Match', img2)

    # Wait for a key press, and if 'q' is pressed, exit the loop and close the window
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
