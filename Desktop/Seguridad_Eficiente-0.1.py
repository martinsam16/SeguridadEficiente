import cv2
import numpy as np 
import time
# import Interfaz
import DibujarRostro

ClasificadorRostro = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
capturar = cv2.VideoCapture(0)

Nombre = 'Desconocido'#Será sustituido por un diccionario Nombres = {"Maria":[x, y]}
nfoto = 0
print "Iniciando..."
while(True):
        a, frame = capturar.read()
        imagen = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        rostro = np.array(ClasificadorRostro.detectMultiScale(imagen, 1.3, 5))

        #registro = open('registro.txt', 'a')

        for (x, y, w, h) in rostro:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (300, 255, 0), 1)
                cv2.putText(frame, Nombre, (x-5, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (300, 255, 0))

                cortar = cv2.resize(np.array(imagen[y:y+h, x:x+w]),(240,240))
                cv2.imshow('Rostros',cortar)

                #print(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')
                #registro.write(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n') 
        
        cv2.imshow('Seguridad Eficiente V-0.1',frame)
        """
        if cv2.waitKey(1) & 0xFF == ord('v'):
                Interfaz.Ventana(Nombre, nfoto, cortar)
                nfoto += 1
        """
        if cv2.waitKey(1) & 0xFF == ord('m'):
                DibujarRostro.Iniciar(cortar)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
                print "Saliendo .."
                capturar.release()
                #registro.close()
                cv2.destroyAllWindows()
                break
exit()