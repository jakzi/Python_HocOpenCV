import speech_recognition as sr #thư viện nhận diện giọng nói 
from gtts import gTTS #Thư viện Chuyển văn bản thành giọng nói 
import playsound #Thư viện phát âm thanh 

r = sr.Recognizer()
with sr.Microphone() as source: #sử dụng micrô mặc định làm nguồn(source ):
    print("Điều chỉnh tiếng ồn ")
    r.adjust_for_ambient_noise(source, duration=1)#lắng nghe trong 1 giây để hiệu chỉnh độ ồn 
    print("Nói bằng tiếng Việt, 5s sau sẽ in ra Text")
    audio_data = r.record(source, duration=5) #nghe trong 5s 
    print("Kết quả nhận diện...")
    try:
        text = r.recognize_google(audio_data,language="vi") #Nhận diện âm thanh tiếng Việt 
    except:
        text = "bạn nói gì mình không hiểu!"
    print("Bạn đã nói là: {}".format(text))
    
def speak(text):
    tts = gTTS(text=text, lang='vi') #chuyển văn bản thành giọng nói(tiếng Việt )
    tenfile = '13NguyenLeHoangThanh.mp3'
    tts.save(tenfile)#lưu file âm thanh 
    playsound.playsound(tenfile)#phát file âm thanh 

speak("Nguyễn Lê Hoàng Thanh ")