import cv2
img1=cv2.imread("Samp_1.jpg")
img2=cv2.imread("Samp_2.jpg")

plainadd=img1+img2
functadd=cv2.add(img1,img2)
weighadd=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow("Samp_1.jpg",img1)
cv2.imshow("Samp_2.jpg",img2)
cv2.imshow("Plain_add",plainadd)
cv2.imshow("Funct_add",functadd)
cv2.imshow("Weigh_add",weighadd)


cv2.waitKey(0)
cv2.destroyAllWindows()