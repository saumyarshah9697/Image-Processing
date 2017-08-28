
# coding: utf-8

# In[1]:

import cv2


# In[6]:

(rAvg,gAvg,bAvg)=(None,None,None)
total=0


stream=cv2.VideoCapture("sample.mp4")


# In[7]:

while True:
    (grabbed,frame)=stream.read()
    if not grabbed:
        break    
    
    else:
        cv2.imshow("Frame",frame)
        cv2.waitKey(1)
        
        
    (B,G,R)=cv2.split(frame.astype("float"))
    
    if rAvg is None:
        rAvg=R
        bAvg=B
        gAvg=G
    
    else:
        rAvg=((total*rAvg)+(1*R))/(total+1.0)
        bAvg=((total*bAvg)+(1*B))/(total+1.0)
        gAvg=((total*gAvg)+(1*G))/(total+1.0)
    total+=1


# In[8]:

avg=cv2.merge([bAvg,gAvg,rAvg]).astype("uint8")
cv2.imshow("Average",avg)
cv2.waitKey(0)
stream.release()


# In[ ]:



