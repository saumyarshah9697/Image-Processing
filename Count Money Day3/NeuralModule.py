from sklearn.neural_network import MLPClassifier
import cv2
import numpy as np
import os
from tqdm import tqdm
import pickle

datasource="numbers/"
def getNPData(img):
    img=cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(img,(8,8))
#     cv2.imshow("number",img)
#     cv2.waitKey(0)
    a=np.array(img);
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
#     np.save('train_data.npy', [training_setX,training_setY])
    return (training_setX,training_setY)

a=createTrainSet(datasource)
clf = MLPClassifier(alpha=1e-5,activation="logistic",hidden_layer_sizes=(100,50))
clf.fit(a[0],a[1])
s=pickle.dumps(clf)
print(clf.predict(getNPData("number.png")))