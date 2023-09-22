import numpy as np
import cv2

cap = cv2.VideoCapture(0)                   #This line initializes a video capture object to capture video from the default camera (index 0). 
                                            #If you have multiple cameras connected, you can specify a different index to choose a different camera.

while True:                   #This loop will continuously capture frames from the camera until you manually terminate the program.
    ret, frame = cap.read()   #Reads a frame from the camera using the cap object. 
                              #It returns two values: ret, which is a Boolean indicating whether the frame was successfully read, and frame, which is the captured frame as a NumPy array.
    
    
    
    width = int(cap.get(3))   #This line gets the width of the captured frame using the get method of the capture object. 
                              #The argument 3 corresponds to the width property.
    
    
    
    height = int(cap.get(4))  #This line gets the height of the captured frame using the get method of the capture object. 
                              #The argument 4 corresponds to the height property.

    image = np.zeros(frame.shape, np.uint8)  #np.zeros(frame.shape, np.uint8) creates a black image of the same dimensions as the input frame. Here's what each part does:
                                             #frame.shape returns a tuple representing the dimensions of the frame image (height, width, and number of channels if it's a color image).
                                             #np.uint8 specifies the data type of the pixel values in the black image. np.uint8 represents unsigned 8-bit integers, which are commonly used to represent pixel values in images.
                                             #So, this line creates a black image (filled with zeros) with the same dimensions as the input frame.


    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)   #fx=0.5 and fy=0.5 specify that the image should be resized to 50% of its original width and 50% of its original height.
                                                                #So, smaller_frame will contain a smaller version of the input image frame with dimensions reduced by 50%.
   
   
   
    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)    #This line displays the resulting image with the title "frame" using OpenCV's imshow function. 
                                  #This will continuously update the displayed image as frames are processed in the loop.

    if cv2.waitKey(1) == ord('q'): # This condition checks if a key was pressed and if that key is 'q'. 
                                   #If the 'q' key is pressed, it breaks out of the loop, effectively ending the video capture.
        break

cap.release()    #After breaking out of the loop, cap.release() is called to release the video capture object, and cv2.destroyAllWindows() is called to close any OpenCV windows.
cv2.destroyAllWindows()


