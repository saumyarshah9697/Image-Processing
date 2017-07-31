import cv2

cap=cv2.VideoCapture("original.mp4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('edit.avi',fourcc, 20.0, (640,480))

count=0
a,frame=cap.read()
count+=1

while count<=440:
    a,frame=cap.read()
    cv2.imshow('frame',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)
    count+=1
    k=cv2.waitKey(1) & 0xFF
    if (k == ord('q')):
        break

out.release()
cap.release()
cv2.destroyAllWindows()