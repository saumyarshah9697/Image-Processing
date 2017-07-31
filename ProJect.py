import cv2


cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,1024)
cap.set(15, -8.0)
counter=0
while True:
    ret, frame=cap.read()
    cv2.imshow("Frame",frame)
    if (counter%150==0):
        cv2.imwrite("images/"+str(counter)+".jpg",frame)
    counter+=1
    k=cv2.waitKey(1) & 0xFF
    if (k == ord('q')):
        break
    


cap.release()
cv2.destroyAllWindows()
