from urllib.request import urlopen
import cv2
import numpy as np
import datetime
import time
from time import sleep
Font=cv2.FONT_HERSHEY_PLAIN
url="http://192.168.0.102:8080/shot.jpg"

count=0
while True:
    imgResp=urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    time=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    cv2.putText(img,time,(0,50), Font,1, (0,0,0), 1, cv2.LINE_AA)
    name="images/Lenovo/"+str(count)+".jpeg"
    cv2.imwrite(name,img)
#     cv2.imshow("IMG",img)
    sleep(5)
    count+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

