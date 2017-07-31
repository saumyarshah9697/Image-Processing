import numpy as np
import cv2




source=cv2.imread("Puzzle.jpg",cv2.COLOR_BGR2GRAY)
target=cv2.imread("Waldo.jpg",cv2.COLOR_BGR2GRAY)
cv2.imshow("Source",source)
(targetH,targetW)=target.shape[:2]

result=cv2.matchTemplate(source,target,cv2.TM_CCOEFF)

(_,_,minLoc,maxLoc)=cv2.minMaxLoc(result)

topLeft=maxLoc
botRight=(topLeft[0]+targetW,topLeft[1]+targetH)
roi=source[topLeft[1]:botRight[1],topLeft[0]:botRight[0]]

mask=np.zeros(source.shape,dtype="uint8")
source=cv2.addWeighted(source,0.25,mask,0.75,0)

source[topLeft[1]:botRight[1],topLeft[0]:botRight[0]]=roi

cv2.imshow("Source2",cv2.resize(source,(800,800)))
cv2.imshow("Target",target)

cv2.waitKey(0)