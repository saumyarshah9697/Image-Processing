import RGBHistogram
import Searcher
import cv2
import pickle
import numpy as np


''' 
First Edit the Indexer.py to provide the path containing various images

Then run this program    
'''
f=open("data.p","rb")
index=pickle.load(f)

path=input("Enter the path")
queryimg=cv2.imread(path)
cv2.imshow("Query",queryimg)


desc=RGBHistogram.RGBHistogram([8,8,8])
queryFeatures=desc.describe(queryimg)

searcher=Searcher.Searcher(index)
results=searcher.search(queryFeatures)


montageA=np.zeros((166*5,400,3),dtype="uint8")
montageB=np.zeros((166*5,400,3),dtype="uint8")


for j in range(0,10):
    (score,imageName)=results[j]
    result=cv2.imread(imageName)
    if j <5:
        montageA[j*166:(j+1)*166,:] =result
        
    else:
        montageB[(j - 5) * 166:((j - 5) + 1) * 166, :] = result

cv2.imshow("Results 1-5", montageA)
cv2.imshow("Results 6-10", montageB)
cv2.waitKey(0)