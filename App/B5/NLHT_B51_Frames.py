# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:30:16 2021

@author: thanh
"""

import cv2 
import os 
import numpy as np 
#B2: KHAI BÁO CÁC HẰNG

INPUT_VIDEO = '13NguyenLeHoangThanh/HongKong.mp4'
OUTPUT_DIR = '13NguyenLeHoangThanh' 

#B3: TẠO THƯ MỤC

os.makedirs(OUTPUT_DIR, exist_ok=True) 
#B4: THỦ TỤC GHÉP Color Frame với Gray Frame (khác biệt)

def nlht_image(img, diff_im):
    new_img = np.zeros([img.shape[0], img.shape[1]*2, img.shape[2]])#ma trận ảnh trống bằng img 
    new_img[:, :img.shape[1], :] = img#img vào bên trái
    #đặt diff_im vào bên phải 
    new_img[:, img.shape[1]:, 0] = diff_im 
    new_img[:, img.shape[1]:, 1] = diff_im
    new_img[:, img.shape[1]:, 2] = diff_im
    cv2.imshow('diff', new_img)
    return new_img
def main(video_path):
    cap = cv2.VideoCapture(video_path) 
    last_gray = None 
    idx = -1
    while(True):
        ret, frame = cap.read() 
        idx += 1
        if not ret: 
            print('Dừng đọc Video vì đã hết (%s)' % video_path)
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#chuyển xám 
        if last_gray is None: 
            last_gray = gray
            continue 
        diff = cv2.absdiff(gray, last_gray)#frame hình khác biệt giữa hình xám trước và sau 
        cv2.imwrite(os.path.join(OUTPUT_DIR, 'NLHT_%06d.jpg' %idx), nlht_image(frame, diff))#ghi ra file 
        last_gray = gray 
        print('Lưu hình thứ : @ %d...' % idx)
        pass
    pass
    cap.release()
    cv2.destroyAllWindows() 
print('Chạy chương trình với video clip %s' % INPUT_VIDEO)
main(video_path=INPUT_VIDEO)