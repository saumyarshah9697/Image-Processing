import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

image=cv2.imread("1.jpg")
img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0
    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
            color.astype("uint8").tolist(), -1)
        startX = endX
    


plt.figure()
plt.axis("off")
plt.imshow(image)

img=img.reshape((img.shape[0]* img.shape[1],3))

clt=KMeans(n_clusters=3)
clt.fit(img)


hist = centroid_histogram(clt)
bar = plot_colors(hist, clt.cluster_centers_)

plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
