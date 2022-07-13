# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:00:45 2021

@author: thanh
"""

import cv2
import os
import speech_recognition as sr
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
    1. Nhập từ video
    2. Nhập từ camera 
            """)
    c=input("Chọn: ")
    if c=="1":
        videos= []
        classNames  = []
        myList = os.listdir(path)#danh sách tệp tin
        #Lấy video và tên
        for cl in myList:
            video= cv2.imread(f'{path}/{cl}',0)
            videos.append(video)
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
            cap = cv2.VideoCapture("{}/{}".format(path,classNames[query]))
        if ch=="2":
            query=int(input("Số thứ tự: "))
            cap = cv2.VideoCapture("{}/{}".format(path,classNames[query]))
    if c=="2":
        cap=cv2.VideoCapture(0)
    return cap
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
    """
    B2: lưu sản phẩm 
    """
    cap=nlht_nhapfile()
    count=0
    frame_name=input("Tên khung hình lưu: ")
    data_adress=input("Thư mục lưu: ")
    os.makedirs(data_adress, exist_ok=True) #Tao thu muc
    
    while True:
        ret,frame = cap.read()
        if not ret or cv2.waitKey(10) & 0xFF == ord('q'): 
            print('Dừng đọc Video vì đã hết')
            break
        cv2.imshow('sdss',frame)
        cv2.imwrite(os.path.join(data_adress, '{}_{}.jpg'.format(frame_name, count )), frame)#Lưu khung hình 
        print('{}_{}.jpg'.format(frame_name, count ))
        count = count + 1 
    cap.release()
    cv2.destroyAllWindows()
    """
    B3: xử lí ảnh 
    """
    images  = []
    images_out = []
    myList = os.listdir(data_adress)
    for cl in myList:
        imgCur= cv2.imread(f'{data_adress}/{cl}')
        images.append(imgCur)

    print("""
___________________________ 
Chọn yêu cầu xử lý : 
    1 .Cắt ảnh theo thông tin về kích thước ảnh được cắt do NSD nhập vào
    2 .Xoay ảnh theo yêu cầu của NSD (NSD nhập yêu câu)
    3 .Thay đổi kích thước ảnh theo yêu cầu của NSD
    """)
    ch  = input("Chọn :  ")
    if ch=="1":
        h1=int(input("Cắt ảnh từ chiều cao:"))
        h2=int(input(" đến "))
        w1=int(input("Cắt ảnh từ chiều rộng :"))
        w2=int(input(" đến "))
        for img in images:
            img=cutimg(img, h1, h2, w1, w2)
            images_out.append(img)   
    if ch=="2":
        g=float(input("Góc xoay theo độ(>0 quay ngược kim đồng hồ ):"))
        for img in images:
            img=rotate(img, g)
            images_out.append(img)   
    if ch=="3":
        s=int(input("Tỉ lệ ảnh: "))
        for img in images:
            img=resize(img, s)
            images_out.append(img)
    temp=0
    os.makedirs(f'{data_adress}/edit', exist_ok=True)#tạo thư mục edit trong thư mục lưu 
   # lưu hình ảnh đã xử lý vào thư mục edit 
    for img in images_out:
        cv2.imwrite(os.path.join(f'{data_adress}/edit', '{}_{}.jpg'.format(frame_name, temp )), img)
        temp+=1
        print('{}_{}.jpg'.format(frame_name, temp ))
    pass

main()
