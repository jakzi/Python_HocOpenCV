# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:03:25 2021

@author: thanh
"""
import cv2 #opencv xử lý hình ảnh 
import os #làm việc với hệ thống 
import speech_recognition as sr # nhận diện giọng nói 
import numpy as np #tính toán 
import matplotlib.image as mpimg #xử lý ảnh cơ bản 
"""
Khai báo hằng 
"""
path = '13NguyenLeHoangThanh'
"""
Nạp fileVideo bằng giọng nói
"""
def nlht_themfile():
    videos= []
    classNames  = [] 
    myList = os.listdir(path)#lấy danh sách tệp tin
    #Lấy video và tên video 
    for cl in myList:
        video= cv2.imread(f'{path}/{cl}',0) #đọc video ở đường dẫn 
        videos.append(video)#thêm vào videos 
        classNames.append(os.path.basename(cl))#thêm tên vào className 
    for i in classNames:#in tên ra màn hình 
        print("{} : {}".format(classNames.index(i),i))
    #Nhận diện giọng nói 
    while (True):
        print("Hãy nói số thứ tự video bạn muốn mở(ví dụ: số 0)")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Điều chỉnh tiếng ồn ")
            r.adjust_for_ambient_noise(source, duration=1)#xử lý tiếng ồn 
            print("Nói bằng tiếng Việt đi bạn 5s sau sẽ in ra Text...")
            audio_data = r.record(source, duration=5)#ghi âm trong 5s 
            print("Kết quả nhận diện...")
            try:
                query = r.recognize_google(audio_data,language="vi") #nhận diện giọng nói 
            except:
                continue 
            print(query)
            query=query.strip('số ')#loại bỏ từ 'số' 
            try:
                query=int(query)# chuyển thành kiểu int 
                break 
            except:   
                continue 
    cap = cv2.VideoCapture("{}/{}".format(path,classNames[query]))#đọc video 
    return cap
"""
Cắt video thành các Frames 
"""
def nlht_catfile():
    cap=nlht_themfile()#gọi nlht_themfile() 
    count=0# đếm khung hình 
    interval=int(input("Interval(mili giây): ")) #khoảng cách khung hình 
    frame_name=input("Tên khung hình lưu: ")
    data_adress=input("Thư mục lưu: ")
    os.makedirs(data_adress, exist_ok=True) #Tao thu muc
    while True:
        ret,frame = cap.read()  
        if not ret: #dừng nếu không còn khung hình 
            print('Dừng đọc Video vì đã hết')
            break
        #lưu khung hình thành ảnh với tên frame_name + count ở data_adress 
        cv2.imwrite(os.path.join(data_adress, '{}_{}.jpg'.format(frame_name, count )), frame)
        cap.set(cv2.CAP_PROP_POS_MSEC, (count*interval)) #đặt thuộc tính cv2.CAP_PROP_POS_MSEC(vị trí hiện tại của khung hình tính bằng mili )
        print('{}_{}.jpg'.format(frame_name, count ))
        count = count + 1 
    cap.release()
    return data_adress
def rotate(img,g):# xoay ảnh 
    (h, w,d) = img.shape # kích thước ảnh 
    center = (w // 2, h // 2)#vị trị giữa 
    M = cv2.getRotationMatrix2D(center, g, 1.0) #ma trận biến đổi theo góc g 
    rotated = cv2.warpAffine(img, M, (w, h))#xoay ảnh 
    return rotated
def cutimg(img,h1,h2,w1,w2):
    p= img[h1:h2,w1:w2]#cắt ảnh 
    return p
def resize(img,s): #thay đổi kích thước 
    (h, w,d) = img.shape
    w=int(w*s/100)
    h=int(h*s/100)
    dim=(w,h)#kích thước mới 
    resized = cv2.resize(img, dim)#thay dổi kích thước ảnh 
    return resized
def rgb_to_gray(img):# chuyển ảnh xám 
        grayImage = np.zeros(img.shape) #tạo ảnh rỗng 
        #lấy ma trận màu  
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])
        #Lấy giá trị màu xám theo The weighted method  
        R = (R *.299)
        G = (G *.587)
        B = (B *.114)
        Avg = (R+G+B)
        
        grayImage = img.copy()
        #chuyển thành ảnh xám 
        for i in range(3):
           grayImage[:,:,i] = Avg
           
        return grayImage
def nlht_suafile(DIR):
    images  = []
    images_out = []#hình ảnh kết quả 
    myList = os.listdir(DIR)#lấy danh sách hình ảnh vừa cắt 
    for cl in myList:
        imgCur= cv2.imread(f'{DIR}/{cl}')#đọc ảnh 
        images.append(imgCur)#thêm vào images 

    print("""
    -------------------------------------
    Chọn chế độ xử lý 
      1.Chuyển ảnh xám
      2.Cắt ảnh theo thông tin về kích thước ảnh được cắt do NSD nhập vào
      3.Xoay ảnh theo yêu cầu của NSD (NSD nhập yêu câu)
      4.Thay đổi kích thước ảnh theo yêu cầu của NSD
    """)
    ch  = input("Chọn ct :  ")
    if ch=="1":
        for cl in myList:
            img= mpimg.imread(f'{DIR}/{cl}')#đọc hình ảnh 
            grayImage = rgb_to_gray(img)#chuyển ảnh xám 
            images_out.append(grayImage)
    if ch=="2":
        h1=int(input("Cắt ảnh từ chiều cao:"))
        h2=int(input(" đến "))
        w1=int(input("Cắt ảnh từ chiều rộng :"))
        w2=int(input(" đến "))
        for img in images:
            img=cutimg(img, h1, h2, w1, w2)#cắt ảnh 
            images_out.append(img)   
    if ch=="3":
        g=float(input("Góc xoay theo độ(>0 quay ngược kim đồng hồ ):"))
        for img in images:
            img=rotate(img, g)#xoay ảnh 
            images_out.append(img)   
    if ch=="4":
        s=int(input("Tỉ lệ ảnh: "))
        for img in images:
            img=resize(img, s)#thay đổi kích thước 
            images_out.append(img)   
    
    size=(images_out[0].shape[1],images_out[0].shape[0])#lấy kích thước khung hình 
    #tạo video sản phẩm với fps = 1 
    out = cv2.VideoWriter('13NguyenLeHoangThanh.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 1,size)
    #ghi hình ảnh vào video để có video kết quả 
    for img in images_out:
        out.write(img)
    out.release()
def main():
    DIR=nlht_catfile()
    nlht_suafile(DIR)
main()
