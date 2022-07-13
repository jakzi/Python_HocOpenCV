import speech_recognition as sr# thư viện nhận diện gọng nói 
from gtts import gTTS # thư viện chuyển văn bản thành giọng nói 
import playsound #thư viện phát âm thanh 
import requests # thư viện cho phép gửi các yêu cầu HTTP 
from requests import get#lấy dữ liệu từ server 



ngonngu=["ar-DZ	","en-US","ja-JP","vi","zh"] #mã các ngôn ngữ của speech_recognition
print("""
      ----------------------
      Chọn ngôn ngữ:
          0 .Tiếng Ả rập
          1 .Tiếng Anh
          2 .Tiếng Nhật
          3 .Tiếng Việt
          4 .Tiếng Trung 
      ----------------------
      """)
c=int(input("Chọn:"))
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Điều chỉnh tiếng ồn  ")
    r.adjust_for_ambient_noise(source, duration=1)#lắng nghe trong 1 giây để hiệu chỉnh độ ồn  
    print("Nói đi bạn 5s sau sẽ in ra Text...")
    audio_data = r.record(source, duration=5) #nghe trong 5s 
    print("Kết quả nhận diện...")
    try:
        text = r.recognize_google(audio_data,language=ngonngu[c])#nhận diện ngôn ngữ đã chọn
    except:
        text = "bạn nói gì mình không hiểu!"
    print("Bạn đã nói là: {}".format(text))
def hoangthanh(text):
    print("""
          ----------------------
          Chọn giọng người nói:
          1.Giọng Nam miền Bắc
          2.Giọng Nữ miền Bắc 
          3.Giọng Nam miền Nam
          4.Giọng Nữ miền Nam
          ----------------------
          """)
    ch=input("Chọn:")
    url = 'https://api.fpt.ai/hmi/tts/v5'#api text to speech của fpt 
    payload = text
    if ch=="1":
        headers = {
            'api-key': 'NG64pRN2TwEiTwRyHiWaT3wDkoTefjLS',
            'speed': '',
            'voice': 'leminh'
        }
    if ch=="2":
        headers = {
    'api-key': 'NG64pRN2TwEiTwRyHiWaT3wDkoTefjLS',
    'speed': '',
    'voice': 'banmaiace'
}
    if ch=="3":
        headers = {
    'api-key': 'NG64pRN2TwEiTwRyHiWaT3wDkoTefjLS',
    'speed': '',
    'voice': 'minhquangace'
}
    if ch=="4":
        headers = {
    'api-key': 'NG64pRN2TwEiTwRyHiWaT3wDkoTefjLS',
    'speed': '',
    'voice': 'linhsansace'
}
    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)#gửi dữ liệu lên url
    jData=response.json()#nhận phản hồi 
    with open("13NguyenLeHoangThanh.mp3", "wb") as file:#tạo file âm thanh 
        r = get(jData["async"])#lấy dữ liệu âm thanh 
        file.write(r.content)#ghi vào file 
    playsound.playsound("13NguyenLeHoangThanh.mp3")#phát file âm thanh
        

def speak(text):
    if ngonngu[c]=="vi":
        hoangthanh(text)
    else:
        tts = gTTS(text=text, lang=ngonngu[c])#chuyển văn bản thành giọng nói 
        filename = '13NguyenLeHoangThanh.mp3'
        tts.save(filename)#lưu file 
        playsound.playsound(filename)

speak(text)