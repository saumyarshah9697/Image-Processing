import cv2 
import time
import numpy as np

# imgpath="G:\\Workspace\\IV Processing\\Samp_4.jpg"
classlabels="G:\Workspace\\IV Processing\\synset_words.txt"
prototxt="G:\\Workspace\\IV Processing\\bvlc_googlenet.prototxt"
model="G:\\Workspace\\IV Processing\\bvlc_googlenet.caffemodel"
cap=cv2.VideoCapture(0)
rows=open(classlabels).read().strip().split("\n")
classes=[r[r.find(" ")+1:].split(",")[0] for r in rows]

net=cv2.dnn.readNetFromCaffe(prototxt,model)

while True:
    ret,image=cap.read()
    blob=cv2.dnn.blobFromImage(image,1, (224, 224), (104, 117, 123))
    net.setInput(blob)
    preds=net.forward()
    idxs = np.argsort(preds[0])[::-1][:5]
    for (i, idx) in enumerate(idxs):
        if i == 0:
            text = "Label: {}, {:.2f}%".format(classes[idx],preds[0][idx] * 100)
            cv2.putText(image, text, (5, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
        
    cv2.imshow("Image",image)
    cv2.waitKey(1)
    
    if ret is None:
        break

