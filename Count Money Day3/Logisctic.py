import cv2
import numpy as np
import os
from tqdm import tqdm
import math


datasource="numbers/"



def HypoThe(Theta,xi):
    if(len(Theta)==len(xi)):
        sum=0
        for i in range(len(xi)):
            sum+=(Theta[i]*xi[i])
        return Sigmoid(sum)
    else:
        return False

def Sigmoid(A):
    return 1/(1+math.exp(A))


def GradTerm(X,Y,Theta,i):
    sum1=0
    for j in range(len(X)):
        if(1-HypoThe(Theta,X[j]))==0:
            term=0
        elif(Y[j]==0):
            term= -(math.log(1-HypoThe(Theta,X[j])))
        else:
            term=-(math.log(HypoThe(Theta, X[j])))
        sum1+=term
    return sum1

def GradDesc(Theta,alpha,Xfeature,Ylabels,lamb):
    Theta_=[]
    Theta_.append(Theta[0]-(GradTerm(Xfeature,Ylabels,Theta,0)*alpha/len(Xfeature)))
    for i in range(1,len(Theta)):
        Theta_.append((Theta[i]*(1-((alpha*lamb)/len(Xfeature))))-(alpha*(GradTerm(Xfeature,Ylabels,Theta,i))/len(Xfeature)))
        if (cv2.waitKey(1)&0xFF)==(ord('q')):
            break        
    return Theta_
    
def LinearRegression(Xfeature,Ylabels,alpha,lamb,iterations):
    if len(Xfeature)!=len(Ylabels):
        print("Missing Data");
        return False
    else:   
        Theta=[]
        for i in range(len(Xfeature)):
            Xfeature[i].insert(0,1)
        for i in range(len(Xfeature[i])):
            Theta.append(0)
        print("========================================================================================")
        
        for i in range(iterations):
            print("\nIteration Number ",i)
            print(Theta)
            
            Theta=GradDesc(Theta, alpha, Xfeature, Ylabels, lamb)
#             Cost=RegCostFunc(Theta, Xfeature, Ylabels, lamb)
            print(Theta)

            print("========================================================================================")
        
        print(Theta)
        return Theta

def getNPData(img):
    img1=cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    img1=cv2.resize(img1,(8,8))
#     cv2.imshow("number",img)
#     cv2.waitKey(0)
    a=np.array(img1);
    temp=[]
    for x in a:
        for y in x:
            temp.append(y)
    return temp

def label_img(img):
    a=int(img.split(".")[0])
#     a=list('{:08b}'.format(a))[4:]
    return a


def createTrainSet(datasource):
    training_setX=[]
    training_setY=[]
    for x in tqdm(os.listdir(datasource)):
        x2=os.path.join(datasource,x)
        y=label_img(x)
        X=getNPData(x2)
        training_setX.append(X)
        training_setY.append(y)
    return (training_setX,training_setY)


def getYLabel(Ydata,K):
    Ylabel=[0]*len(Ydata)
    for a in range(len(Ydata)):
        if Ydata[a]==K:
            Ylabel[a]=1
    return Ylabel

def Predict(THETA,XTest):
    XTest=getNPData(XTest)
    Y=[0]*len(THETA)
    for i in range(len(THETA)):
        Y.append(HypoThe(THETA[i], XTest))
    return Y.index(max(Y))


iterations=int(input("Enter the Number of Iterations"))
alpha=float(input("Enter the learning rate"))
lamb=float(input("Enter the regularization term"))
Xfeature,Ydata=createTrainSet(datasource)
mi,ma=min(Ydata),max(Ydata)
K=ma-mi+1

THETA=[]
for i in range(K):
    Ylabels=getYLabel(Ydata, K)
    THETA.append(LinearRegression(Xfeature, Ylabels, alpha, lamb, iterations))

print(Predict(THETA,"number.bmp"))
