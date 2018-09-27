#Importando librerias
import cv2#Visión Artificial
import numpy as np #Procesamiento con matrices

#Importando Archivos clasificadores
clasificador_ojo=cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')
clasificador_rostro=cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
capturar=cv2.VideoCapture(0) #Inicializar cámara (n) es el número de cámara escogida

while(True):#Bucle infinito
        a, frame = capturar.read()#leo con la camara seleccionada:a es booleano, frame es un cuadro
        imagen=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#cambiar colores a escala de grises y guardar en variable imagen
        ojos = clasificador_ojo.detectMultiScale(imagen, 1.3, 5)
        rostro = clasificador_rostro.detectMultiScale(imagen, 1.3, 5)

        for (x,y,w,h) in ojos:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),3) #(x1,y1) - vertices del cuadro
        for (x,y,w,h) in rostro:
                cortar= imagen[y:y+h, x:x+w]#Cortar coordenadas seleccionadas
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),5)
                cv2.putText(frame, 'Nombre', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(300, 255, 0))#Insertar texto

        cv2.imshow('Seguridad Eficiente', frame) #Crear ventana con: (nombre de la ventana, objeto a mostrar)

        if cv2.waitKey(1) & 0xFF == ord('g'):#Esperar que una tecla se presione y que esta sea la 'g'
                cv2.imwrite('img/captura.png',cortar)#Escribir o guardar imagen (poner nombre y la extensión, imagen)
        elif cv2.waitKey(1) & 0xFF == ord('s'):#Esperar que una tecla se presione y que esta sea la 's'
                break#Saltar bucle

capturar.release()#Liberando recursos
#cv2.destroyWindow('Seguridad Eficiente')
cv2.destroyAllWindows()#Cerrar todas las ventanas creadas
