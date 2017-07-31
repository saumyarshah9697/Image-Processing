import cv2


def Flip(frame):
    rows,columns=frame.shape[0:2]
    Mirrored=cv2.cvtColor(frame,cv2.IMREAD_COLOR)
    for x in range(rows):
        for y in range(columns):
            Mirrored[x][columns-y-1]=frame[x][y]
    return Mirrored

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow("Original",frame)
    frame=Flip(frame)
    cv2.imshow("Mirrored",frame)
    k=cv2.waitKey(1) & 0xFF
    if (k == ord('m')):
        cv2.destroyWindow("Mirrored")
    if (k == ord('o')):
        cv2.destroyWindow("Original")
    if (k == ord('a')):
        break

cap.release()
cv2.destroyAllWindows()


