import numpy as np
import cv2

cap = cv2.VideoCapture(0) 

while True:                   
    ret, frame = cap.read()   
    
    width = int(cap.get(3))  
    
    height = int(cap.get(4)) 

    img=cv2.line(frame,(0,0),(width,height),(255,0,0),10)

'''cv2.line--->>>  Draws two lines on the frame. 
One line goes from the top-left corner (0,0) to the bottom-right corner (width,height) with a blue color (255,0,0)
 and a thickness of 10 pixels. 
 The other line goes from the bottom-left corner (0,height) to the top-right corner (width,0) 
 with a red color (0,0,255) and a thickness of 3 pixels.'''

    img=cv2.line(frame,(0,height),(width,0),(0,0,255),3)
    img=cv2.rectangle(frame,(100,100),(400,300),(0,100,0),5)  # Draws a green rectangle on the frame with the top-left corner at (100,100), 
                                                              #the bottom-right corner at (400,300), and a thickness of 5 pixels.
    
    
    img=cv2.circle(frame,(200,200),(150),(112,118,120),-1) #Draws a filled circle with a center at (200,200), 
                                                           #a radius of 150 pixels, and a gray color (112,118,120).   (-1) is to fill it,can fill it with any other integer to decribe it's thickness!

   
   
    font = cv2.FONT_HERSHEY_SIMPLEX  # Selects the font type for the text.
    img = cv2.putText(frame, 'Benson Loves Real Madrid!!!', (10, height - 10), font, 1, (0, 0, 0), 5, cv2.LINE_AA)

'''Adds the text "Benson Loves Real Madrid!!!" to the frame at coordinates (10, height - 10)
 with the selected font, a font scale of 1, a black color (0,0,0), 
 a thickness of 5 pixels, and using the anti-aliased cv2.LINE_AA line type.'''

    cv2.imshow('frame', img) #Displays the frame with the drawn shapes and text in a window with the title "frame."

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()    
cv2.destroyAllWindows()