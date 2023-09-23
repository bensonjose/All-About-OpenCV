import numpy as np
import cv2

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)  # Draws a blue line from top-left to bottom-right
    
    img = cv2.line(frame, (0, height), (width, 0), (0, 0, 255), 3)  # Draws a red line from bottom-left to top-right
    img = cv2.rectangle(frame, (100, 100), (400, 300), (0, 100, 0), 5)  # Draws a green rectangle
    
    img = cv2.circle(frame, (200, 200), 150, (112, 118, 120), -1)  # Draws a filled gray circle
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frame, 'Benson Loves Real Madrid!!!', (10, height - 10), font, 1, (0, 0, 0), 5, cv2.LINE_AA)  # Adds text

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
