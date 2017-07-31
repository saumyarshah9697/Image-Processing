import numpy as np
import _pickle as cPickle
import cv2
import pickle

class Searcher:
    def __init__(self,index):
        self.index=index    
        
    def chi2distance(self,histA,histB,eps=1e-10):    
        d=0.5*np.sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(histA,histB)])
        return d
        
    def search(self,queryFeatures):
        results={}
        
        for (k,features) in self.index.items():
            d=self.chi2distance(features,queryFeatures)
            
            results[k]=d
            
        results=sorted([(v,k) for (k,v) in results.items() ])
        return results
#     
# f=open("data.p","rb")
# # index=cPickle.loads(open("data.txt","rb").read())
# index=pickle.load(f)
# searcher=Searcher(index)
# path=input("Enter the path")
# img=cv2.imread(path)
# cv2.imshow("Query",img)
#     
# for (query,queryFeatures) in index.items():
#     results=searcher.search(queryFeatures)
#     
#     montageA=np.zeros((166*5,400,3),dtype="uint8")
#     montageB=np.zeros((166*5,400,3),dtype="uint8")
#     
#     for j in range(0,10):
#         (score,imageName)=results[j]
#         result=cv2.imread(imageName)
#         
#         if j <5:
#             montageA[j*166:(j+1)*166,:] =result
#         else:
#             montageB[(j-5)*166:((j-5)+1)*166,:]=result
#             
# cv2.imshow("Results 1-5",montageA)
# cv2.imshow("Result 6-10",montageB)
# cv2.waitKey(0)