print "Iniciando..."
import cv2
import numpy as np 
import time
# import Interfaz
import DibujarRostro

capturar = cv2.VideoCapture(0)
ClasificadorRostro = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')

cortar = cv2.cvtColor(cv2.resize(cv2.imread("img/Demo.jpg"),(240,240)),cv2.COLOR_BGR2GRAY)

Nombre = 'Desconocido'#Será sustituido por un diccionario Nombres = {"Maria":[x, y]}
#nfoto = 0
while(True):
        a, frame = capturar.read()
        imagen = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        rostro = np.array(ClasificadorRostro.detectMultiScale(imagen, 1.3, 5))

        if cv2.waitKey(1) & 0xFF == ord('s'):
                print "Saliendo .."
                capturar.release()
                #registro.close()
                cv2.destroyAllWindows()
                break
        if cv2.waitKey(1) & 0xFF == ord('m'):
                DibujarRostro.Iniciar(cortar)
        #registro = open('registro.txt', 'a')
        #registro.write(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')

        for (x, y, w, h) in rostro:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (300, 255, 0), 1)
                cv2.putText(frame, Nombre, (x-5, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (300, 255, 0))
                cortar = cv2.resize(np.array(imagen[y:y+h, x:x+w]),(240,240))
                
        cv2.imshow('Rostro',cortar)
        cv2.imshow('Seguridad Eficiente V-0.1',frame)              
        
        """#Guardar
        if cv2.waitKey(1) & 0xFF == ord('g'):
                #Interfaz.Ventana(Nombre, nfoto, cortar)
                cv2.imwrite('img/'+Nombre+str(nfoto)+'.png', cortar)
                nfoto += 1
        """
exit()