import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,0,0])
    upper_red=np.array([255,77,255])
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Camera",frame)
    cv2.imshow("Mask",mask)
    
    cv2.imshow("res",res)
    
    k=cv2.waitKey(1 )& 0xFF
    
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break

cap.release()