import RGBHistogram
import os
import cv2
import _pickle as cPickle
import pickle
from tqdm import tqdm
IndexPath="images"
IndexImages=os.listdir(IndexPath)

index={}
desc=RGBHistogram.RGBHistogram([8,8,8])

for i in tqdm(IndexImages):
    j=os.path.join(IndexPath,i)
    img=cv2.imread(j)
    features=desc.describe(img)
    index[j]=features
    
f=open("data.p","wb")

pickle.dump(index,f)

