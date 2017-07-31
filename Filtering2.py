import cv2
import numpy as np
def FILT():
    pass



while True:
    
#     cap=cv2.VideoCapture("C:/Users/Saumya/Videos/15s.mp4")
    cap=cv2.VideoCapture(0)
    cv2.namedWindow('res')
    cv2.createTrackbar('l1','res',0,255,FILT)
    cv2.createTrackbar('l2','res',0,255,FILT)
    cv2.createTrackbar('l3','res',0,255,FILT)
    cv2.createTrackbar('u1','res',0,255,FILT)
    cv2.createTrackbar('u2','res',0,255,FILT)
    cv2.createTrackbar('u3','res',0,255,FILT)

    ret, frame=cap.read()
    frame=cv2.resize(frame,(50,50))
    while ret:
        l1 = cv2.getTrackbarPos('l1','res')
        l2 = cv2.getTrackbarPos('l2','res')
        l3 = cv2.getTrackbarPos('l3','res')
        u1 = cv2.getTrackbarPos('u1','res')
        u2 = cv2.getTrackbarPos('u2','res')
        u3 = cv2.getTrackbarPos('u3','res')
    
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_red=np.array([l1,l2,l3])
        upper_red=np.array([u1,u2,u3])
    
        mask=cv2.inRange(hsv,lower_red,upper_red)
        res=cv2.bitwise_and(frame,frame,mask=mask)
        
        cv2.imshow("res",res)
    
        k=cv2.waitKey(1 )& 0xFF
        if(k==ord('q')):
            cv2.destroyAllWindows()
            break

        ret, frame=cap.read()
    cap.release()