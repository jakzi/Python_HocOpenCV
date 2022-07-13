import speech_recognition as sr #thư viện nhận diện giọng nói 

final_text=""
while True:
    print("Nói 'bắt đầu' để bắt đầu, 'chấm hết' để kết thúc")
    r = sr.Recognizer()
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Điều chỉnh tiếng ồn ")
        r.adjust_for_ambient_noise(source, duration=1)#lắng nghe trong 1 giây để hiệu chỉnh độ ồn 
        print("Nói bằng tiếng Việt, 5s sau sẽ in ra Text...")
        audio_data = r.record(source, duration=5)#nghe trong 5s 
        print("Kết quả nhận diện...")
        try:
            query = r.recognize_google(audio_data,language="vi")#Nhận diện âm thanh tiếng Việt 
            print(query)
            if 'bắt đầu' in query:#nghe được 'bắt đầu' sẽ thực hiện  
                with sr.Microphone() as source2 :
                    r2.adjust_for_ambient_noise(source2 , duration=1)#lắng nghe trong 1 giây để hiệu chỉnh độ ồn  
                    print("Đang nghe")
                    audio =r2.listen(source )#nghe đến khi dừng nói 
                    try:
                        text = r2.recognize_google(audio,language="vi")#nhận diện ngôn ngữ tiếng Việt 
                    except:
                        text = ""
                final_text+=" " +text#nối văn bản nghe được vào kết quả 
                print("{}".format(final_text))
                continue 
            if 'chấm hết' in query:#nghe được 'chấm hết' sẽ thực hiện chương trình sau 
                print("Văn bản của bạn:")
                print("{}".format(final_text))
                print("Kết thúc chương trình")
                break
        except:
            continue 

    pass

    