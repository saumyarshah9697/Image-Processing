import BirdEyeView as BDV
import cv2
import numpy as np





image=cv2.imread("1.jpg")
# _,image=cv2.VideoCapture(0).read()
image=cv2.resize(image,(800,600))
heightratio=image.shape[0]/500
orig=image.copy()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1),(5,5),0)
edged=cv2.Canny(gray,75,20)

# cv2.imshow("Image",image)
# cv2.imshow("Edged",edged)


(_,cnts, _)=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

for c in cnts:
#     ScreenCnt=[]
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*peri,True)
    print(len(approx))
    if len(approx)==4:
        ScreenCnt=approx
        break
        cv2.drawContours(image,[ScreenCnt],-1,(0,255,0),2)
        


cv2.drawContours(image,[ScreenCnt],-1,(0,255,0),2)
# cv2.imshow("Outline",image)

warped=BDV.four_point_transform(orig, ScreenCnt.reshape(4,2))

warped=cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
# warped = cv2.adaptiveThreshold(warped, 251,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)
# ret, warped=cv2.threshold(warped,70,190,cv2.THRESH_BINARY)
# warped = warped.astype("uint8") * 255


cv2.imshow("Original",orig)
cv2.imshow("Scanned", cv2.resize(warped,(warped.shape[0],orig.shape[1])))




cv2.waitKey(0)
cv2.destroyAllWindows()

    