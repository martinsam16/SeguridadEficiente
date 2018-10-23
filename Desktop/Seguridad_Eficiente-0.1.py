print ("Iniciando...")
import cv2, numpy as np, pickle
#DibujarRostro

ClasificadorRostro = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')


recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/face-trainner.yml")

labels={"person_name":1}
with open("pickle/face-labels.pickle",'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}
capturar = cv2.VideoCapture(0)
roi_gray=cv2.imread('img/martin/martin0.jpg')
	
#txt = open('txt/nFoto.txt', 'r')
nfoto=0
#txt.close()

while(True):
        ret, frame = capturar.read()
        gray  = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        rostro = np.array(ClasificadorRostro.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5))
        
        #registro = open('txt/registro.txt', 'a')
        #registro.write(time.strftime("ROSTRO IDENTIFICADO    - Fecha: %d/%m/%y"+" Hora: %H:%M:%S")+'\n')
        for (x, y, w, h) in rostro:
                roi_gray=np.array(gray[y:y+h, x:x+w])
                roi_color=np.array(frame[y:y+h, x:x+w])
                id_, conf = recognizer.predict(np.array(roi_gray))
                if conf>=8 and conf <= 85:
                        cv2.putText(frame, labels[id_], (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (500, 600, 10), 1, cv2.LINE_AA)
                        cv2.rectangle(frame, (x, y), (x + w,  y + h), (500, 600, 10), 1)
                else:
                        cv2.rectangle(frame, (x, y), (x + w,  y + h),(900, 0, 900), 3 )
        cv2.imshow('Rostro',cv2.resize(roi_gray,(120,120),dst=None))
        cv2.imshow('Seguridad Eficiente V-0.1',cv2.resize(frame,(500,300),dst=None))
        if cv2.waitKey(20) & 0xFF == ord('s'):
                print ("Saliendo ..")
                #txt = open('txt/nFoto.txt', 'w')
                #txt.write(str(nfoto))
                #txt.close()
                capturar.release()
                #registro.close()
                cv2.destroyAllWindows()
                break

        #if cv2.waitKey(1) & 0xFF == ord('m'):
         #       print ("Mostrando...")
          #      DibujarRostro.Iniciar(cortar)
           #     print ("Mostrado")

        if cv2.waitKey(20) & 0xFF == ord('g'):
                print ("Guardando...")
                cv2.imwrite('img/james/james'+str(nfoto)+'.jpg',roi_gray)
                print ("Guardado.")
                nfoto +=1
exit()
