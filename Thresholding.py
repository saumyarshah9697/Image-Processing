import cv2

img1=cv2.imread("ToProcess.jpeg")
cv2.imshow("Original",img1)

img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY SCALE",img2)

ret, img3=cv2.threshold(img1,220,255,cv2.THRESH_BINARY  )
cv2.imshow("Plain Threshold",img3)

ret, img4=cv2.threshold(img2,220,255,cv2.THRESH_BINARY)
cv2.imshow("Plain Threshold2",img4)

img5=cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("Adaptive Threshold",img5)

cv2.waitKey(0)
cv2.destroyAllWindows()