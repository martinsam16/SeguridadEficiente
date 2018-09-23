import cv2
import numpy as np
#import matplotlib.pyplot as plt

clasificador_ojo=cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')
clasificador_rostro=cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
capturar=cv2.VideoCapture(0)

while(True):
        a, frame = capturar.read()
        imagen=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ojos = clasificador_ojo.detectMultiScale(imagen, 1.3, 5)
        rostro = clasificador_rostro.detectMultiScale(imagen, 1.3, 5)
        for (x,y,w,h) in ojos:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),3)
        for (x,y,w,h) in rostro:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),5)
        cv2.imshow('Seguridad Eficiente', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
                break
capturar.release()
cv2.destroyAllWindows()
