# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:35:10 2021

@author: thanh
"""

import cv2 # opencv xử lý hình ảnh

cap = cv2.VideoCapture("13NguyenLeHoangThanh/HongKong.mp4") #mở video 
count = 0  #biến đếm khung hình 
while cap.isOpened(): #Kiểm tra mở được video hay không 
    ret,frame = cap.read() # đọc khung hình, chuẩn bị khung tiếp theo 
    cv2.imshow('Khung Hinh', frame)#hiển thị hình ảnh 
    cv2.imwrite("Khung%d.jpg" %count, frame)#lưu hình ảnh vào tệp
    count = count + 1 
    if cv2.waitKey(10) & 0xFF == ord('q'):# chờ phím q được nhấn thì dừng
        break
cap.release()
cv2.destroyAllWindows()
    
