import cv2
import numpy as np
import time


def FILT():
    pass

counter=0
cv2.namedWindow('res',1)
cv2.createTrackbar('y1','res',0,776,FILT)
cv2.createTrackbar('y2','res',776,776,FILT)
cv2.createTrackbar('x1','res',0,1376,FILT)
cv2.createTrackbar('x2','res',1376,1376,FILT)

while True:
    cap=cv2.VideoCapture("C:/Users/Saumya/Videos/15s.mp4")
    ret, frame1=cap.read()
    frame=frame1[:,:]
    while True:
        frame[:-1,:-1]=(0,0,0)
        l1 = 44
        l2 = 492
        u1 = 682
        u2 = 1168
 
        l1 = cv2.getTrackbarPos('y1','res')
        l2 = cv2.getTrackbarPos('y2','res')
        u1 = cv2.getTrackbarPos('x1','res')
        u2 = cv2.getTrackbarPos('x2','res')
        frame=frame1[l1:l2,u1:u2]
        print(frame.shape)
        print(frame1.shape)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_red=np.array([0,0,0])
        upper_red=np.array([255,77,255])
        time.sleep(2)
        mask=cv2.inRange(hsv,lower_red,upper_red)
        res=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("Camera",frame)
        cv2.imshow("Mask",mask)
        
        cv2.imshow("res",res)
        ret, frame1=cap.read()
        cv2.imwrite("images/"+str(counter)+".jpeg",frame)
        counter+=1
        k=cv2.waitKey(1 )& 0xFF
        if(k==ord('q')):
            cv2.destroyAllWindows()
            break
cap.release()