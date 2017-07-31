import cv2
import numpy as np


Font=cv2.FONT_HERSHEY_PLAIN

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# cap=cv2.VideoCapture("15s.mp4")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        cap=cv2.VideoCapture(0)
        ret,frame=cap.read()
        
    cv2.resize(frame,(300,300))
    (rects,weights)=hog.detectMultiScale(frame,winStride=(4,4),padding=(16, 16),scale=1.05)
    cv2.putText(frame,str(len(rects)),(0,50), Font,1, (255,255,255), 1, cv2.LINE_AA)
    
    
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
        
    cv2.imshow("Video",frame)
    k= (cv2.waitKey(1)& 0xFF)
    if k==ord("q"):
        break;
    
      
