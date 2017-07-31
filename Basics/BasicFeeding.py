import cv2
cap=cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,1024)
cap.set(15, -8.0)

Font=cv2.FONT_HERSHEY_PLAIN
while True:
    ret, frame=cap.read()
    imgF=cv2.cvtColor(frame,cv2.IMREAD_COLOR)
    cv2.putText(frame,"Press Q to Capture Colour",(0,50), Font,1, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(frame,"Press W to Capture Gray Scale",(0,100), Font,1, (255,255,255), 1, cv2.LINE_AA)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1) & 0xFF
    if (k == ord('q')):
        break
    elif (k == ord('w')):
        imgF=cv2.cvtColor(imgF,cv2.COLOR_BGR2GRAY)
        break
    else:
        continue

cap.release()
cv2.destroyAllWindows()
# img=cv2.imread("BasicImage.jpg")
# cv2.imshow("Image",img)
# cv2.waitKey(0)
cv2.imshow("Last Captured Frame",imgF)
cv2.waitKey(0)
cv2.destroyAllWindows()