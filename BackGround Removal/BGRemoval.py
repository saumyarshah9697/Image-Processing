import cv2
import os
from time import sleep
import numpy as np

cap=cv2.VideoCapture("C:/Users/Saumya/Videos/15s.mp4")
cap=cv2.VideoCapture(0)
bgsub=cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((15,15),np.float32)/225
counter=0
ret, frame = cap.read()
while ret:
    frame=cv2.resize(frame,(500,500))
    fgmask = bgsub.apply(frame)
    x=fgmask
    Revfgmask=cv2.bitwise_not(fgmask)
    cv2.imshow('frame',frame)
    cv2.imshow('BGSubbed',fgmask)
    cv2.imshow('RevBGSubbed',Revfgmask)
    cv2.imshow('MaskedRevBGSubbed',cv2.bitwise_and(frame,frame,mask=Revfgmask))
    cv2.imshow('MaskedBGSubbed',cv2.bitwise_and(frame,frame,mask=fgmask))
    cv2.imshow('Regular',cv2.filter2D(fgmask,-1,kernel))                   #Regular Blur
    cv2.imshow('Gaussian',cv2.GaussianBlur(fgmask,(15,15),0))               #Gaussian Blur
    cv2.imshow('Median',cv2.medianBlur(fgmask,5))                         #Median Blur
    cv2.imshow('Bilateral',cv2.bilateralFilter(fgmask,15,75,75))             #Bilateral Blur
    cv2.imwrite("images/"+str(counter)+".jpeg",x)
    input()
    sleep(2)
    counter+=1
    ret, frame = cap.read()
    k=cv2.waitKey(1 )& 0xFF    
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break

cap.release()