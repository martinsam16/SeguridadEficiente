#Importando librerias
import cv2#Visión Artificial
import numpy as np #Procesamiento con matrices
import time

#Importando Archivos clasificadores
clasificador_ojo=cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')
clasificador_rostro=cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
capturar=cv2.VideoCapture(0) #Inicializar cámara (n) es el número de cámara escogida

nfoto=0
NombrePerson='Demo'
while(True):#Bucle infinito
        a, frame = capturar.read()#leo con la camara seleccionada:a es booleano, frame es un cuadro
        imagen=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#cambiar colores a escala de grises y guardar en variable imagen
        ojos = clasificador_ojo.detectMultiScale(imagen, 1.3, 5)
        rostro = clasificador_rostro.detectMultiScale(imagen, 1.3, 5)

        registro = open('registro.txt','a')// a escribe desde el final, w bora y escribe

        for (x,y,w,h) in ojos:#Vertices del cuadro y coordenadas
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),3)
                registro.write(str(time.strftime("OJO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S"))+'\n')
        for (x,y,w,h) in rostro:
                cortar= imagen[y:y+h, x:x+w]#Cortar coordenadas seleccionadas
                cv2.imshow('Rostros', cortar)
                registro.write(str(time.strftime("ROSTRO IDENTIFICADO - Fecha: %d/%m/%y"+" Hora: %H:%M:%S"))+'\n')
                
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),5)
                cv2.putText(frame, NombrePerson, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(300, 255, 0))#Insertar texto

        cv2.imshow('Seguridad Eficiente', frame) #Crear ventana con: (nombre de la ventana, objeto a mostrar)
        
        if cv2.waitKey(1) & 0xFF == ord('g'):#Esperar que una tecla se presione y que esta sea la 'g'
                cv2.imwrite('img/'+NombrePerson+str(nfoto)+'.png',cortar)#Escribir o guardar imagen (poner nombre y la extensión, imagen)
                nfoto+=1
        elif cv2.waitKey(1) & 0xFF == ord('s'):#Esperar que una tecla se presione y que esta sea la 's'
                break#Saltar bucle

capturar.release()#Liberando recursos
registro.close()
#cv2.destroyWindow('Seguridad Eficiente')#Cerrar la ventana que tiene (este nombre)
cv2.destroyAllWindows()#Cerrar todas las ventanas creadas
