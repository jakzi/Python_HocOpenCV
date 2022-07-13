# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:12:11 2021

@author: thanh
"""

import speech_recognition as sr# nhận diện âm thanh
from googletrans import Translator # google dịch 

ngonngu=['ar','en','ja','zh-cn']#mã ngôn ngữ của googletrans 
r = sr.Recognizer()
with sr.Microphone() as source:#chọn micro làm nguồn 
    print("Điều chỉnh tiếng ồn  ")
    r.adjust_for_ambient_noise(source, duration=1)# điều chỉnh tiếng ồn 
    print("Nói bằng tiếng Việt đi bạn 5s sau sẽ in ra Text...")
    audio_data = r.record(source, duration=5)# ghi âm 
    print("Kết quả nhận diện...")
    try:
        text = r.recognize_google(audio_data,language="vi")# chuyển thành text 
    except:
        text = "bạn nói gì mình không hiểu!"
    print("Bạn đã nói là: {}".format(text))


print("""
      ----------------------
      Chọn ngôn ngữ:
          0 .Tiếng Ả rập
          1 .Tiếng Anh
          2 .Tiếng Nhật
          3 .Tiếng Trung 
      ----------------------
      """)
c=int(input("Chọn:"))
translator = Translator()
translated = translator.translate(text,dest=ngonngu[c],src='auto')#dịch 
print(translated.text)