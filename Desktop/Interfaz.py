from Tkinter import *
import cv2


def Ventana(Nombre,nfoto,cortar):
    ventana=Frame(height=150,width=400)
    ventana.pack(padx=20,pady=20)
    boton=Button(ventana, text="Guardar",command=Cerrar(Nombre,nfoto,cortar),font=("Verdana",5),height=6,width=6)
    boton.pack()
    ventana.mainloop()
    
def Cerrar(Nombre,nfoto,cortar):
    cv2.imwrite('img/'+Nombre+str(nfoto)+'.png',cortar)