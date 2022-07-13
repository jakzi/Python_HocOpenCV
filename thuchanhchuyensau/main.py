import cv2
import numpy as np
import os
import shutil

path = 'KhoAnh'
#orb= cv2.ORB_create(nfeatures=1000)
brisk = cv2.BRISK_create()

#Thêm hình ảnh
images  = []
classNames  = []
print("Them anh vao kho?(Y/N):")
i= input()
if i == 'Y':
    while True:
        print("Duong dan file:")
        x = input()
        shutil.copy2(x, path)
        print("Tiep tuc them file(Y/N):")
        y=input()
        if y == 'N':
            break
myList = os.listdir(path)#danh sách tệp tin
#print('So anh: ',len(myList))

#Lấy ảnh và tên
for cl in myList:
    imgCur= cv2.imread(f'{path}/{cl}',0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
def findDes(images):
    desList=[]
    for img in images:
        #kp,des = orb.detectAndCompute(img,None)
        kp, des = brisk.detectAndCompute(img, None)
        desList.append(des)
    return desList
def findID(img, desList,thres=30):
    #kp2,des2=orb.detectAndCompute(img,None)
    kp2, des2 = brisk.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList=[]
    finalVal =-1
    try:
        for des in desList:
            matches = bf.knnMatch(des,des2,k=2)
            good=[]
            for m,n in matches:
                if m.distance <0.75*n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass
    #print(max(matchList))
    if len(matchList)!=0:
        if max(matchList) > thres:
            finalVal= matchList.index(max(matchList))
    return  finalVal


c=input('Camera:  0\nVideo :  1\n')
if c == '0' :
    cap= cv2.VideoCapture('https://192.168.50.120:8080/video')
    if cap.isOpened()!= True :
        cap = cv2.VideoCapture(0)
if c == '1' :
    x = input('Duong dan file:')
    cap = cv2.VideoCapture(x)

desList = findDes(images)
while True:
    success, img2 = cap.read()
    imgOri= img2.copy()
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    id= findID(img2,desList)
    if id != -1:
        cv2.putText(imgOri,classNames[id],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

    cv2.imshow('img2',imgOri)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)
cap.release()
cv2.destroyAllWindows()
"""
        sift = cv2.SIFT_create()
        kp=[];des=[]
        for i in range(len(images)):
            kp[i], des[i] = sift.detectAndCompute(images[i],None)
        img = self.img_out
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kp, des = sift.detectAndCompute(gray,None)
        bf = cv2.BFMatcher()
"""
