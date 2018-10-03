#Importando librerias
import cv2#Visión Artificial
import dlib
import numpy as np #Procesamiento con matrices
import time
import matplotlib.pyplot as plt
#import serial

#Importando Archivos clasificadores
clasificador_ojo=cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')
clasificador_rostro=cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
capturar=cv2.VideoCapture(0) #Inicializar cámara (n) es el número de cámara escogida

#Importando Detector
detector= dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("Predictors/shape_predictor_68_face_landmarks.dat")
nfoto=0
Nombre='Nombre'
while(True):#Bucle infinito
        a, frame = capturar.read()#leo con la camara seleccionada:a es booleano, frame es un cuadro
        imagen=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#cambiar colores a escala de grises y guardar en variable imagen

        ojos = clasificador_ojo.detectMultiScale(imagen, 1.3, 5)
        rostro = clasificador_rostro.detectMultiScale(imagen, 1.3, 5)

#Landmarks
        clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(6,6))
        clahe_image = clahe.apply(imagen)
        detections = detector(clahe_image, 1)

        registro = open('registro.txt','a')# a escribe desde el final, w bora y escribe

        for k,d in enumerate(detections):
                shape = predictor(clahe_image, d)
                for i in range(1,68):
                        cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (300,255,0), thickness=1)
                        plt.scatter(shape.part(i).y,shape.part(i).x)
        plt.show()

        for (x,y,w,h) in rostro:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),1)
                cortar= imagen[y:y+h, x:x+w]#Cortar coordenadas seleccionadas
                cv2.imshow('Rostro', cortar)
                
                #print(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')
                registro.write(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')         
                
                cv2.putText(frame, Nombre, (x-5, y-5), cv2.FONT_HERSHEY_PLAIN,1,(300, 255, 0))#Insertar texto

        cv2.imshow('Seguridad Eficiente V-0.1', frame) #Crear ventana con: (nombre de la ventana, objeto a mostrar)
        
        if cv2.waitKey(1) & 0xFF == ord('g'):#Esperar que una tecla se presione y que esta sea la 'g'
                cv2.imwrite('img/'+Nombre+str(nfoto)+'.png',cortar)#Escribir o guardar imagen (poner nombre y la extensión, imagen)
                nfoto+=1
        if cv2.waitKey(1) & 0xFF == ord('s'):#Esperar que una tecla se presione y que esta sea la 's'
                break#Saltar bucle
        time.sleep(1)

capturar.release()#Liberando recursos
registro.close()
#cv2.destroyWindow('Seguridad Eficiente')#Cerrar la ventana que tiene (este nombre)
cv2.destroyAllWindows()#Cerrar todas las ventanas creadas
exit()
