# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:47:36 2021

@author: thanh
"""

import cv2 # opencv xử lý hình ảnh
import os #tương tác với hệ điều hành

def menu():#menu đầu tiên 
    print("Nhập lựa chọn : ")
    print("1.Nạp ảnh màu ")
    print("2.Nạp ảnh xám ")
    ch  = input("Chọn ct :  ")
    return ch 
def iput():#nhập đường dẫn 
    path=input("Nhập đường dẫn file ảnh: ")
    #kiểm tra file có tồn tại hay không 
    if os.path.exists(path):
        print("exists.")
    else:
        print("not exists.")
        iput()
    return path
def submenu1():#Menu nạp ảnh màu 
    print("""
          Chọn chức năng:
          1.1.Chuyển ảnh xám
          1.2.Lấy kích thước ảnh
          1.3.Cắt ảnh theo thông tin về kích thước ảnh được cắt do NSD nhập vào
          1.4.Xoay ảnh theo yêu cầu của NSD (NSD nhập yêu câu)
          1.5.Lấy giá trị màu của điểm ảnh tại vị trí NSD chọn với hệ màu RGB
          1.6.Thay đổi kích thước ảnh theo yêu cầu của NSD
    """)
    ch  = input("Chọn chức năng :  ")
    return ch 
def submenu2():#Menu nạp ảnh xám 
    print("""
          Chọn chức năng : 
          2.1.Lấy kích thước ảnh
          2.2.Cắt ảnh theo thông tin về kích thước ảnh được cắt do NSD nhập vào
          2.3.Xoay ảnh theo yêu cầu của NSD (NSD nhập yêu câu)
          2.4.Lấy giá trị màu của điểm ảnh tại vị trí NSD chọn(màu xám)
    """)
    ch  = input("Chọn chức năng :  ")
    return ch 
def imgsize(img,mau):#kích thước ảnh 
   if mau==1:# kích thước ảnh màu 
       (h, w, d) = img.shape
       print("width={}, height={}, depth={}".format(w, h, d))
   if mau==0:#kích thước ảnh xám 
       (h, w) = img.shape
       print("width={}, height={}".format(w, h))
def cutimg(img):#cắt ảnh 
    h1=int(input("Cắt ảnh từ chiều cao:"))
    h2=int(input(" đến "))
    w1=int(input("Cắt ảnh từ chiều rộng :"))
    w2=int(input(" đến "))
    p= img[h1:h2,w1:w2]
    cv2.imshow('Cat',p)
def rotate(img,mau):#xoay ảnh 
    if mau == 1:# lấy kích thước ảnh màu 
        (h, w, d) = img.shape
    if mau == 0:# lấy kích thước ảnh xám 
       (h, w) = img.shape
    center = (w // 2, h // 2)# lấy điểm giữa ảnh 
    g=float(input("Góc xoay theo độ(>0 quay ngược kim đồng hồ ):"))
    M = cv2.getRotationMatrix2D(center, g, 1.0) # ma trận biến đổi theo góc g 
    rotated = cv2.warpAffine(img, M, (w, h))#xoay ảnh theo ma trận 
    cv2.imshow('Xoay',rotated)
def getcolor(img,mau):# lấy màu tại 1 điểm 
    x=int(input("Giá trị tọa độ x của điểm: "))
    y=int(input("Giá trị tọa độ y của điểm: "))
    if mau==1:# lấy màu ảnh màu 
        (B, G, R) = img[x,y]
        print("Blue={},Green={},Red={}".format(B,G,R))
    if mau==0:# lấy màu ảnh xám 
        print("Gray:",img[x,y])
def resize(img):# thay đổi kích thước ảnh 
    (h, w, d) = img.shape# kích thước ảnh màu 
    imgsize(img, 1)
    s=int(input("Tỉ lệ ảnh: "))
    w=int(w*s/100)
    h=int(h*s/100)
    dim=(w,h)#kích thước mới 
    resized = cv2.resize(img, dim)#thay đổi kích thước 
    imgsize(resized,1)
    cv2.imshow('TiLe',resized)
while True:
    ch=menu()   
    if ch=="1":
        path=iput()
        img = cv2.imread(path)
        ch1=submenu1()
        if ch1=="1":
            imgGray = cv2.imread(path,cv2.IMREAD_GRAYSCALE)# đọc ảnh xám 
            cv2.imshow('Xam',imgGray)
            cv2.imshow('Goc',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if ch1=="2":
            imgsize(img,1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if ch1=="3":
            cutimg(img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if ch1=="4":
            rotate(img,1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if ch1=="5":
            getcolor(img, 1)
        if ch1=="6":
            resize(img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    if ch=="2":
        path=iput()
        img= cv2.imread(path,cv2.IMREAD_GRAYSCALE)# đọc ảnh xám 
        ch2=submenu2()
        if ch2=="1":
            imgsize(img,0)
        if ch2=="2":
            cutimg(img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if ch2=="3":
            rotate(img,0)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if ch2=="4":
            getcolor(img, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()