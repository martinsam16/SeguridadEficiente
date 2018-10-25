print ("Iniciando...")
import cv2, numpy as np, pickle

ClasificadorRostro = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("entrenamiento/trainner.yml")

labels={"nombrepersona":1}
with open("entrenamiento/labels.pickle",'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}
        
capturar = cv2.VideoCapture(0)
cortar=[]

nfoto=0

while(True):
        booleano, frame = capturar.read()
        frameBN  = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        rostro = np.array(ClasificadorRostro.detectMultiScale(frameBN, scaleFactor=1.5, minNeighbors=5))

        for (x, y, w, h) in rostro:

                cortar=np.array(frameBN[y:y+h, x:x+w])
                cv2.imshow('Rostro',cv2.resize(cortar,(120,120),dst=None))
                
                id_, conf = recognizer.predict(np.array(cortar))

                if conf>=30 and conf <= 100:
                        cv2.putText(frame, labels[id_], (x,y), cv2.FONT_HERSHEY_PLAIN, 3, (500, 600, 10), 2, cv2.LINE_AA)
                        cv2.rectangle(frame, (x, y), (x + w,  y + h), (500, 600, 10), 1)
                else:
                        cv2.putText(frame, "Desconocido", (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (900, 0, 900), 1, cv2.LINE_AA)
                        cv2.rectangle(frame, (x, y), (x + w,  y + h),(900, 0, 900), 1 )
                        print ("ALERTA")
        
        cv2.imshow('Seguridad Eficiente V-0.1',cv2.resize(frame,(500,400),dst=None))

        if cv2.waitKey(20) & 0xFF == ord('g'):
                print ("Guardando...")
                cv2.imwrite('img/martin/martin'+str(nfoto)+'.jpg',cortar)
                print ("Guardado.")
                nfoto +=1

        if cv2.waitKey(20) & 0xFF == ord('s'):
                print ("Saliendo ..")
                capturar.release()
                cv2.destroyAllWindows()
                break

exit()
