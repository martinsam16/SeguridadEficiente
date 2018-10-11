print "Iniciando..."
import cv2, numpy as np, DibujarRostro

capturar = cv2.VideoCapture(0)
ClasificadorRostro = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')

cortar = cv2.cvtColor(cv2.resize(cv2.imread("img/Demo.jpg"),(140,140)),cv2.COLOR_BGR2GRAY)

Nombre = 'Desconocido'#Será sustituido por un diccionario Nombres = {"Maria":[x, y]}

txt = open('txt/nFoto.txt', 'r')
nfoto=int(txt.read())
txt.close()

while(True):
        a, frame = capturar.read()
        imagen = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        rostro = np.array(ClasificadorRostro.detectMultiScale(imagen, 1.3, 5))

        if cv2.waitKey(1) & 0xFF == ord('s'):
                print "Saliendo .."
                txt = open('txt/nFoto.txt', 'w')
                txt.write(str(nfoto))
                txt.close()
                capturar.release()
                #registro.close()
                cv2.destroyAllWindows()
                break
        #registro = open('txt/registro.txt', 'a')
        #registro.write(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')
        for (x, y, w, h) in rostro:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (300, 255, 0))
                cv2.putText(frame, Nombre, (x-5, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (300, 255, 0))
                cortar = np.array(imagen[y:y+h, x:x+w])
        cortar=np.array(cv2.resize(cortar,(140,140)))

        cv2.imshow('Rostro',cortar)
        cv2.imshow('Seguridad Eficiente V-0.1',cv2.resize(frame,(400,300)))

        if cv2.waitKey(1) & 0xFF == ord('m'):
                print "Mostrando..."
                DibujarRostro.Iniciar(cortar)
                print "Mostrado"

        if cv2.waitKey(1) & 0xFF == ord('g'):
                print "Guardando..."
                cv2.imwrite('img/'+Nombre+str(nfoto)+'.png', cortar)
                print "Guardado."
                nfoto +=1
exit()