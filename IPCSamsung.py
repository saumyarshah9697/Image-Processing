from urllib.request import urlopen
import cv2
import numpy as np
import datetime
import time
from time import sleep
from selenium import webdriver


dr=webdriver.Chrome()
Font=cv2.FONT_HERSHEY_PLAIN
url="http://192.168.0.105:8080/shot.jpg"
dr.get("http://192.168.0.105:8080/")
el=dr.find_element_by_id("flashbtn")

count=0
while True:
    el.click()
    sleep(5)
    imgResp=urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    el.click()
    img=cv2.imdecode(imgNp,-1)
    time=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    cv2.putText(img,time,(0,50), Font,1, (255,255,255), 1, cv2.LINE_AA)
    name="images/Samsung/"+str(count)+".jpeg"
    cv2.imwrite(name,img)
    sleep(5)
#    cv2.imshow("IMG",img)
    sleep(5)
    count+=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

