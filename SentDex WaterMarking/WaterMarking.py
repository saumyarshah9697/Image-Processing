import cv2

imglogo=cv2.imread("sentdex.png")
cv2.imshow("Logo",imglogo)
image_to_watermark_on=cv2.imread("Samp_1.jpg")
cv2.imshow("Initial",image_to_watermark_on)


rows,columns,channels=imglogo.shape
roi=image_to_watermark_on[10:rows+10,10:columns+10]

imglogoG=cv2.cvtColor(imglogo,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grey",imglogoG)

ret, fg_mask=cv2.threshold(imglogoG,220,255,cv2.THRESH_BINARY_INV)
# cv2.imshow("ForeGround Mask",fg_mask)

bg_mask = cv2.bitwise_not(fg_mask)
# cv2.imshow("Background Mask",bg_mask)

img_back=cv2.bitwise_and(roi,roi,mask=bg_mask)
# cv2.imshow("Img_back",img_back)

img_fore=cv2.bitwise_and(imglogo,imglogo,mask=fg_mask)
# cv2.imshow("Img_fore",img_fore)

final_image=cv2.add(img_back,img_fore)
image_to_watermark_on[10:rows+10,10:columns+10]=final_image
cv2.imshow("Final",image_to_watermark_on)

cv2.waitKey(0)
cv2.destroyAllWindows()