#import cv2
#cap= cv2.VideoCapture(0)#'D:\HOC TAP\Tai lieu\Audio\#San - Cầu Hôn (Cover).mp4'
#while (cap.isOpened()):
#    ret, frame=cap.read()
#    w= int(frame.shape[1]*1.2)
#    h= int(frame.shape[0]*1.2)
#    frame=cv2.resize(frame,(w,h))
#    frame=cv2.Canny(frame,100,200)
#    frame = cv2.flip(frame, 1)
#    cv2.imshow('view',frame)
#    if cv2.waitKey(1) & 0xFF == 27: #27==ESC, ord('A') == A
#        break
#cap.release()
#cv2.destroyAllWindows()
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
