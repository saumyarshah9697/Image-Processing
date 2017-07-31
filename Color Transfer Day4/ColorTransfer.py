import cv2
import numpy as np

def colorTransfer(source,target):
    source=cv2.cvtColor(source,cv2.COLOR_BGR2LAB).astype("float32")
    target=cv2.cvtColor(target,cv2.COLOR_BGR2LAB).astype("float32")
    
    (lMeanSrc,lStdSrc,aMeanSrc,aStdSrc,bMeanSrc,bStdSrc)=image_stats(source)
    (lMeanTar,lStdTar,aMeanTar,aStdTar,bMeanTar,bStdTar)=image_stats(target)
    (l,a,b)=cv2.split(target)
    
    l-=lMeanTar
    a-=aMeanTar
    b-=bMeanTar
    
    l=(lStdTar/lStdSrc)*l
    a=(aStdTar/aStdSrc)*a
    b=(bStdTar/bStdSrc)*b
    
    l+=lMeanSrc
    a+=aMeanSrc
    b+=bMeanSrc
    
    l=np.clip(l,0,255)
    a=np.clip(a,0,255)
    b=np.clip(b,0,255)
    
    transfer=cv2.merge([l,a,b])
    transfer=cv2.cvtColor(transfer.astype("uint8"),cv2.COLOR_LAB2BGR)                            
    
    return transfer
    

def image_stats(image):
    (l,a,b)=cv2.split(image)
    (lMean, lStd)=(l.mean(), l.std())
    (aMean, aStd)=(a.mean(), a.std())
    (bMean, bStd)=(b.mean(), b.std())
    return(lMean,lStd,aMean,aStd,bMean,bStd)
    


src=cv2.resize(cv2.imread("source.jpg"),(768,512))
tar=cv2.resize(cv2.imread("target.jpg"),(768,512))

# src=cv2.imread("source.jpg")
# tar=cv2.imread("target.jpg")

tra=colorTransfer(src, tar)
cv2.imshow("Source",src)
cv2.imshow("Target",tar)
cv2.imshow("Transfer",tra)
cv2.waitKey(0)
cv2.destroyAllWindows()