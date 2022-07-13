# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:01:37 2021

@author: thanh
"""
import cv2 
import speech_recognition as sr
import os
import numpy as np
"""
Khai báo hằng 
"""
path = '13NguyenLeHoangThanh'
"""
Nạp fileVideo bằng giọng nói
"""
def nlht_nhapfile():
    print("""
___________________________
Chọn chế độ nhập: 
    1. Nhập từ image
    2. Nhập từ camera 
            """)
    c=input("Chọn: ")
    if c=="1":
        anh = []
        classNames  = []
        myList = os.listdir(path)#danh sách tệp tin
        #Lấy anh và tên
        for cl in myList:
            img = cv2.imread(f'{path}/{cl}',0)
            anh.append(img)
            classNames.append(os.path.basename(cl))#lấy tên tệp tin 
        for i in classNames:#liệt kê file 
            print("{} : {}".format(classNames.index(i),i))
        print("""
___________________________
Chọn chế độ nhập:        
    1. Dùng giọng nói
    2. Nhập số thứ tự 
              """)
        ch=input("Chọn: ") 
        if ch=="1":
            while (True):
                print("Hãy nói số thứ tự video bạn muốn mở(ví dụ: số 0)")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Điều chỉnh tiếng ồn ")
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Nói bằng tiếng Việt đi bạn 5s sau sẽ in ra Text...")
                    # read the audio data from the default microphone
                    audio_data = r.record(source, duration=5)
                    print("Kết quả nhận diện...")
                    # convert speech to text
                    try:
                        query = r.recognize_google(audio_data,language="vi")
                    except:
                        continue 
                    print(query)
                    query=query.strip('số ')#bỏ từ 'số' 
                    try:
                        query=int(query)
                        break 
                    except:   
                        continue 
            imgout = cv2.imread("{}/{}".format(path,classNames[query]),cv2.IMREAD_COLOR)
        if ch=="2":
            query=int(input("Số thứ tự: "))
            imgout = cv2.imread("{}/{}".format(path,classNames[query]),cv2.IMREAD_COLOR)
    if c=="2":
        cap=cv2.VideoCapture(0)
        while(cap.isOpened()):
            ret, frame = cap.read()
            cv2.imshow('Bam q de chup',frame)
            if cv2.waitKey(10) & 0xFF == ord('q'): 
                cv2.imwrite('thanh_camera.jpg',frame)
                break
        cap.release()
        cv2.destroyAllWindows()
        imgout = cv2.imread('thanh_camera.jpg',cv2.IMREAD_COLOR)
    return imgout
def apply_sliding_window(img, kernel, padding=0, stride=1): 
    h, w = img.shape[:2]
    img_p = np.zeros([h+2*padding, w+2*padding]) 
    img_p[padding:padding+h, padding:padding+w] = img 
    kernel = np.array(kernel) # lập cửa sổ trượt
    assert len(kernel.shape) == 2 and kernel.shape[0] == kernel.shape[1]
    assert kernel.shape[0] % 2 != 0
    
    k_size = kernel.shape[0] 
    k_half = int(k_size/2)
    
    y_pos = [v for idx, v in enumerate(list(range(k_half, h-k_half))) if idx % stride == 0] 
    x_pos = [v for idx, v in enumerate(list(range(k_half, w-k_half))) if idx % stride == 0] 
    
    new_img = np.zeros([len(y_pos), len(x_pos)]) 
    for new_y, y in enumerate(y_pos):
        for new_x, x in enumerate(x_pos):
            if k_half == 0: 
                pixel_val = img_p[y, x] * kernel 
            else:
                pixel_val = np.sum(img_p[y-k_half:y-k_half+k_size, x-k_half:x-k_half+k_size] * kernel)          
            new_img[new_y, new_x] = pixel_val
    return new_img
def apply_sliding_window_on_3_channels(img, kernel, padding=0, stride=1):	#làm mờ ảnh
    layer_blue = apply_sliding_window(img[:,:,0], kernel, padding, stride) 
    layer_green = apply_sliding_window(img[:,:,1], kernel, padding, stride) 
    layer_red = apply_sliding_window(img[:,:,2], kernel, padding, stride)
    new_img = np.zeros(list(layer_blue.shape) + [3])
    new_img[:,:,0], new_img[:,:,1], new_img[:,:,2] = layer_blue, layer_green, layer_red 
    return new_img
def nhapthamso():
    print("Nhập tham số :")
    print("+Window size (kernel size): kích thước cửa sổ trượt = là số lẻ, tức 3, 5, 7, …")
    kernel=int(input())
    print("+ Padding: số pixel mở rộng thêm vào ảnh đầu vô (thường 0, 1, 2, 3, …)")
    padding=int(input())
    print("+ Stride: khoảng cách lần trượt (thường 0, 1, 2, 3, …)")
    stride=int(input())
    print("+ Dilation: khoảng cách của mỗi pixel trên cửa sổ (thường 0, 1, 2, 3, …)")
    dilation=int(input())
    return kernel,padding,stride,dilation
"""
def thaydoikichthuoc(img,ty_le):#kernel= 1 ,stride= 100/ti le=> anh thu nho theo ti le
    padding=0
    p=ty_le/100
    (kernel,stride)=p.as_integer_ratio()
    newimg=apply_sliding_window_on_3_channels(img, [[kernel]],padding,stride)
    return newimg
"""
def rotate(img,g):#xoay ảnh 
    (h, w,d) = img.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, g, 1.0) 
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated
def cutimg(img,h1,h2,w1,w2):#cắt ảnh 
    p= img[h1:h2,w1:w2]
    return p
def resize(img,s):#thay đổi kích thước 
    (h, w,d) = img.shape
    w=int(w*s/100)
    h=int(h*s/100)
    dim=(w,h)
    resized = cv2.resize(img, dim)
    return resized
def main():
    img=nlht_nhapfile()
    img_name=input("Tên file lưu: ")
    data_adress=input("Thư mục lưu: ")
    os.makedirs(data_adress, exist_ok=True) #Tao thu muc
    print("""
___________________________ 
Chọn yêu cầu xử lý : 
    1 .Cắt ảnh theo thông tin về kích thước ảnh được cắt do NSD nhập vào
    2 .Xoay ảnh theo yêu cầu của NSD (NSD nhập yêu câu)
    3 .Thay đổi kích thước ảnh theo yêu cầu của NSD
    4 .Chinh anh theo kernel,padding,stride nhap vao
    5 .Lam mo anh
    """)
    
    ch  = input("Chọn :  ")
    if ch=="1":
        h1=int(input("Cắt ảnh từ chiều cao:"))
        h2=int(input(" đến "))
        w1=int(input("Cắt ảnh từ chiều rộng :"))
        w2=int(input(" đến "))
        newimg=cutimg(img, h1, h2, w1, w2)
    if ch=="2":
        g=float(input("Góc xoay theo độ(>0 quay ngược kim đồng hồ ):"))
        newimg=rotate(img, g)
    if ch=="3":
        s=int(input("Tỉ lệ ảnh: "))
        newimg=resize(img, s)
    if ch=="4":
        (kernel,padding,stride,dilation)=nhapthamso()
        newimg=apply_sliding_window_on_3_channels(img, [[kernel]],padding,stride)
    if ch=="5":
        newimg=apply_sliding_window_on_3_channels(img, [[1]],padding=0,stride=2)
    print("Dang luu...")
    cv2.imwrite(os.path.join(data_adress, '{}.jpg'.format(img_name)), newimg)
    print("Hoan thanh xu li")
main()

    