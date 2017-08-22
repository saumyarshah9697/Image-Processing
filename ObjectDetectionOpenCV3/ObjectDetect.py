import cv2 
import time
import numpy as np

imgpath="G:\\Workspace\\IV Processing\\Mordor-005.png"
classlabels="G:\Workspace\\IV Processing\\synset_words.txt"
prototxt="G:\\Workspace\\IV Processing\\bvlc_googlenet.prototxt"
model="G:\\Workspace\\IV Processing\\bvlc_googlenet.caffemodel"
image= cv2.imread(imgpath)

rows=open(classlabels).read().strip().split("\n")
classes=[r[r.find(" ")+1:].split(",")[0] for r in rows]

blob=cv2.dnn.blobFromImage(image,1, (224, 224), (104, 117, 123))

net=cv2.dnn.readNetFromCaffe(prototxt,model)

net.setInput(blob)
start = time.time()
preds=net.forward()
end=time.time()
print("{:.5} seconds".format(end-start))

idxs = np.argsort(preds[0])[::-1][:5]

for (i, idx) in enumerate(idxs):
    if i == 0:
        text = "Label: {}, {:.2f}%".format(classes[idx],preds[0][idx] * 100)
        cv2.putText(image, text, (5, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
    print("[INFO] {}. label: {}, probability: {:.5}".format(i + 1,classes[idx], preds[0][idx]))

cv2.imshow("Image",image)
cv2.waitKey(0)

