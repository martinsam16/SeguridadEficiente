
import cv2
import numpy as np 
import time
import Interfaz
import DibujarRostro

clasificador_rostro=cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
capturar=cv2.VideoCapture(0)
nfoto=0
Nombre='Nombre'#Será sustituido por un diccionario Nombres={"Maria":[x,y]}

while(True):#Bucle infinito
        a, frame = capturar.read()#leo con la camara seleccionada:a es booleano, frame es un cuadro
        imagen=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#cambiar colores a escala de grises y guardar en variable imagen

        rostro = clasificador_rostro.detectMultiScale(imagen, 1.3, 5)

        registro = open('registro.txt','a')# a escribe desde el final, w bora y escribe
   
        if cv2.waitKey(1) & 0xFF == ord('m'):
                DibujarRostro.Iniciar(imagen,frame)

        for (x,y,w,h) in rostro:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),1)
                cortar= imagen[y:y+h, x:x+w]#Cortar coordenadas seleccionadas
                cv2.imshow('Rostro', cortar)
                print(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')
                registro.write(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')         
                cv2.putText(frame, Nombre, (x-5, y-5), cv2.FONT_HERSHEY_PLAIN,1,(300, 255, 0))#Insertar texto

        cv2.imshow('Seguridad Eficiente V-0.1', frame) #Crear ventana con: (nombre de la ventana, objeto a mostrar)
        
        if cv2.waitKey(1) & 0xFF == ord('v'):
                Interfaz.Ventana(Nombre,nfoto,cortar)
                nfoto+=1
        if cv2.waitKey(1) & 0xFF == ord('s'):
                print "Saliendo .."
                capturar.release()
                registro.close()
                cv2.destroyAllWindows()
                break
exit()

