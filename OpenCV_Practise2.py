import cv2

# Load an image from a file.
img = cv2.imread(r"E:\Desktop Wallpapers\Chevrolet-Camaro-wp.jpg")

# Resize the image to half its original size.
resized_img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Copy a region of interest (ROI) from the resized image.
tag = resized_img[50:100, 75:150]

# Paste the copied ROI back into the resized image at a different location.
resized_img[25:75, 25:100] = tag

# Display the modified, smaller resized image

# Open a window to display the image with the title "Image"
cv2.imshow('Image', resized_img)

# Wait for a key press indefinitely (0) or for a specific time (in milliseconds)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()




# Copied Image shown at top left of the Output.
