import cv2

img=cv2.imread("E:\Desktop Wallpapers\spiderman 2 wp.jpg",1)   #Loading the Image
img=cv2.resize(img,(400,400))                                  #Resizing the Image if needed
img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)             #Rotating the Image if needed
cv2.imshow('Image',img)                                        #To Display the Image and to mention name of the window that'll be displayed
cv2.waitKey(5000)                                              #Mentions how long the window stays open Ex-->5000ms=5s
cv2.destroyAllWindows()                                        #Closes the Window

# cv2.imwrite('new_img.jpg',img)   #This is to write image into a new file.
