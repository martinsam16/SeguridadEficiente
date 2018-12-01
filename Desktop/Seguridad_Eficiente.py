import cv2, numpy as np, pickle, re

def IniciarIdentificacion():
        try:
                nfoto = 0
                ClasificadorRostro = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
                
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                video = cv2.VideoWriter('vid/video.avi', fourcc, 10.0, (640, 480))
                
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                recognizer.read("entrenamiento/matrices.yml")

                labels = {"nombrepersona":0}
                with open("entrenamiento/etiquetas.pickle", 'rb') as f:
                        og_labels = pickle.load(f)
                        labels = {v:k for k, v in og_labels.items()}
                        
                capturar = cv2.VideoCapture(0)
                cortar = []

                nombre = "Demo"
                margen = 25

                while(not cv2.waitKey(20) & 0xFF == ord('s')):
                        booleano, frame = capturar.read()
                        frameBN  = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
                        rostro = np.array(ClasificadorRostro.detectMultiScale(frameBN, scaleFactor = 1.5, minNeighbors = 5))

                        for (x, y, w, h) in rostro:
                                cortar = np.array(frameBN[y:y+h, x:x+w])
                                cv2.imshow('Rostro', cv2.resize(cortar, (200, 200), dst = None))
                                
                                id_, conf = recognizer.predict(np.array(cortar))
                                nombre = labels[id_]
                                nombre = nombre[0:len(nombre)-4]
                                nombre = re.sub("\d", "", nombre)
                                if conf > margen :
                                        cv2.putText(frame, nombre , (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (500, 600, 10), 1, cv2.LINE_AA)
                                        cv2.rectangle(frame, (x, y), (x + w,  y + h), (500, 600, 10), 1)
                                        cv2.circle(frame, (x+30, y+30), 5, [500, 600, 10], -1)
                                else:
                                        nombre = "Intruso"
                                        cv2.putText(frame, nombre , (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (900, 0, 900), 1, cv2.LINE_AA)
                                        cv2.rectangle(frame, (x, y), (x + w,  y + h), (900, 0, 900), 1 )
                                        print ("ALERTA")
                        
                        if (booleano):
                                video.write(np.array(frame))
                        
                        cv2.imshow('Seguridad Eficiente V_0.2', cv2.resize(frame, (800, 600), dst = None))

                        if (cv2.waitKey(20) & 0xFF == ord('g')):
                                cv2.imwrite('img/quispe/quispe'+str(nfoto)+'.jpg', cortar)
                                print ("Guardado.")
                                nfoto += 1 
                cv2.destroyAllWindows()
                #video.release()
                capturar.release()               

        except Exception as e:
                print(e)
                pass



"""
# Funcion para la ventana guardar fotos
nfoto = 0
def tomar_foto():
        cv2.imwrite('img/saman/saman'+str(nfoto)+'.jpg', cortar)
        print ("Guardado.")
        nfoto += 1
root = Tk()
Button(root, text = 'Capturar', command = TomarFoto).pack()
root.mainloop()

def crear_carpeta(nombre):
 os.mkdir("./img/"+nombre)
 
def eliminar_carpeta(nombre):
  shu.rmtree("./img"+nombre)
  
def ingresar_datos():
        pass

def iniciar_ventana(imagen, nombre):
    root = tkint.Tk()
    btn = tkint.Button(root, text = "Registrar", command = IngresarDatos())
    btn.pack()
    root.mainloop()
"""
