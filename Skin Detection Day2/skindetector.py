import numpy as np
import cv2



''' IV Processing>>Filtering2 '''

import cv2
import numpy as np
def FILT():
    pass

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
bgsub=cv2.createBackgroundSubtractorMOG2()
while True:
    
    cap=cv2.VideoCapture(0)
    cv2.namedWindow('res')
    cv2.createTrackbar('l1','res',0,255,FILT)
    cv2.createTrackbar('l2','res',0,255,FILT)
    cv2.createTrackbar('l3','res',0,255,FILT)
    cv2.createTrackbar('u1','res',0,255,FILT)
    cv2.createTrackbar('u2','res',0,255,FILT)
    cv2.createTrackbar('u3','res',0,255,FILT)

    ret, frame=cap.read()
    frame=cv2.resize(frame,(500,500))
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
        res=cv2.GaussianBlur(mask,(3,3),0)
        res = cv2.erode(res, kernel, iterations = 2)
        res = cv2.dilate(res, kernel, iterations = 2)
        res=cv2.bitwise_and(frame,frame,mask=res)
#         res=cv2.medianBlur(res,5)
#         res=cv2.bilateralFilter(res,15,75,75)
#         res= bgsub.apply(frame)
#         res=cv2.bitwise_and(frame,frame,mask=res)
        cv2.imshow("res",res)
    
        k=cv2.waitKey(1 )& 0xFF
        if(k==ord('q')):
            cv2.destroyAllWindows()
            break

        ret, frame=cap.read()
    cap.release()