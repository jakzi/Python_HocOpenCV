import speech_recognition as sr #thư viện nhận diện giọng nói 
def hoangthanh():#Nhận diện giọng nói nhập dữ liệu
    while (True):
        print("Hãy nói số thứ tự bạn muốn chọn (ví dụ: số 0)")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Điều chỉnh tiếng ồn  ")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Nói bằng tiếng Việt đi bạn 5s sau sẽ in ra Text...")
            # nghe âm thanh trong 5s 
            audio_data = r.record(source, duration=5)
            print("Kết quả nhận diện...")
            # nhận diện giọng nói 
            try:
                query = r.recognize_google(audio_data,language="vi")
            except:
                continue 
            print(query)
            query=query.strip('số ')#cắt 'số' khỏi text
            try:
                break 
            except:   
                continue 
    return query
while True:
    print("""
    ----------------------
    Chọn chương trình: 
        1.Phương trình bậc 2
        2.Diện tích hình tròn 
    ----------------------
          """)
    ans = hoangthanh()
    print("""
    ----------------------
    Chọn ngôn ngữ chương trình:
    1.Python
    2.C++
    3.Java
    ----------------------
    """)
    ans2 = hoangthanh()
    #Mở file theo lựa chọn
    if ans=="1" and ans2 =="1":
        print("PT2 python")
        f = open("PT2Python.txt",encoding="utf8", mode="r")
        for line in f:
            print(line)
        f.close()
    if ans=="1" and ans2 =="2":
        print("PT2 C++")
        f = open("PT2C++.txt",encoding="utf8", mode="r")
        for line in f:
            print(line)
        f.close()
    if ans=="1" and ans2 =="3":
        print("PT2 Java")
        f = open("PT2Java.txt",encoding="utf8", mode="r")
        for line in f:
            print(line)
        f.close()
    if ans=="2" and ans2 =="1":
        print("Dien tich hinh tron python")
        f = open("DTHTPython.txt",encoding="utf8", mode="r")
        for line in f:
            print(line)
        f.close()
    if ans=="2" and ans2 =="2":
        print("Dien tich hinh tron C++")
        f = open("DTHTC++.txt",encoding="utf8", mode="r")
        for line in f:
            print(line)
        f.close()
    if ans=="2" and ans2 =="3":
        print("Dien tich hinh tron Java")
        f = open("DTHTJava.txt",encoding="utf8", mode="r")
        for line in f:
            print(line)
        f.close()

    

         

    