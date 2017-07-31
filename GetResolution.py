import cv2
import numpy as np


cap=cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1024)
# cap.set(15, -8.0)

ret, frame=cap.read()
cv2.imshow("frame",frame)
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
imgarray=np.asarray(frame)
width,height=0,0
for x in imgarray:
    height+=1
    width=0
    for y in x:
        width+=1

print("RESOLUTION IS ",width,"x",height)
print(frame.size)
print(frame.shape)