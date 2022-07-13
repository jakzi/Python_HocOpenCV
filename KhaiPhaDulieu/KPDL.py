import cv2
import numpy as np

img1 = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("2.jpg", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("3.jpg", cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread("4.jpg", cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread("5.jpg", cv2.IMREAD_GRAYSCALE)
img6 = cv2.imread("6.jpg", cv2.IMREAD_GRAYSCALE)



sift = cv2.SIFT_create()


kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
kp3, des3 = sift.detectAndCompute(img3,None)
kp4, des4 = sift.detectAndCompute(img4,None)
kp5, des5 = sift.detectAndCompute(img5,None)
kp6, des6 = sift.detectAndCompute(img6,None)

print("Duong dan:")
path=input()
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kp, des = sift.detectAndCompute(gray,None)
bf = cv2.BFMatcher()
dem1=0
dem2=0
dem3=0
dem4=0
dem5=0
dem6=0
matches = bf.knnMatch(des1,des, k=2)
for m,n in matches:
    if m.distance < 0.75*n.distance:
        dem1=dem1+1
matches = bf.knnMatch(des2,des, k=2)
for m,n in matches:
    if m.distance < 0.75*n.distance:
        dem2=dem2+1
matches = bf.knnMatch(des3,des, k=2)
for m,n in matches:
    if m.distance < 0.75*n.distance:
        dem3=dem3+1
matches = bf.knnMatch(des4,des, k=2)
for m,n in matches:
    if m.distance < 0.75*n.distance:
        dem4=dem4+1
matches = bf.knnMatch(des5,des, k=2)
for m,n in matches:
    if m.distance < 0.75*n.distance:
        dem5=dem5+1
matches = bf.knnMatch(des6,des, k=2)
for m,n in matches:
    if m.distance < 0.75*n.distance:
        dem6=dem6+1

A=max([dem1,dem2,dem3,dem4,dem5,dem6])
if A == dem1 :
    cv2.imshow("1", img1)
if A == dem2 :
    cv2.imshow("2", img2)
if A == dem3 :
    cv2.imshow("3", img3)
if A == dem4 :
    cv2.imshow("4", img4)
if A == dem5 :
    cv2.imshow("5", img5)
if A == dem6 :
    cv2.imshow("6", img6)
cv2.imshow("I", img)

    
#print(des.shape)
#img=cv2.drawKeypoints(gray,kp,None)
#cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


