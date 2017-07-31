import cv2
import numpy as np
import time


def FILT():
    pass

counter=0
cv2.namedWindow('res',0)
cv2.createTrackbar('y1','res',0,776,FILT)
cv2.createTrackbar('y2','res',776,776,FILT)
cv2.createTrackbar('x1','res',0,1376,FILT)
cv2.createTrackbar('x2','res',1376,1376,FILT)

while True:
    cap=cv2.VideoCapture("C:/Users/Saumya/Videos/15s.mp4")
    ret, frame=cap.read()
    
    while ret:
        l1 = cv2.getTrackbarPos('y1','res')
        l2 = cv2.getTrackbarPos('y2','res')
        u1 = cv2.getTrackbarPos('x1','res')
        u2 = cv2.getTrackbarPos('x2','res')
        
        frame=frame[l1:l2,u1:u2]
        
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_red=np.array([0,0,0])
        upper_red=np.array([255,77,255])
        time.sleep(2)
        mask=cv2.inRange(hsv,lower_red,upper_red)
        res=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("Camera",frame)
        cv2.imshow("Mask",mask)
    
        cv2.imshow("res",res)
        cv2.imwrite("images/"+str(counter)+".jpeg",res)
        k=cv2.waitKey(1 )& 0xFF
        ret, frame=cap.read()
        if(k==ord('q')):
            cv2.destroyAllWindows()
        break
        counter+=1
cap.release()