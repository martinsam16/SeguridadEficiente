from Tkinter import *
import cv2

def ventana(Nombre, nfoto, cortar):
    ventana = Tk()
    ventana = Frame(height = 150, width = 400)
    ventana.pack(padx = 20, pady = 20)
    boton = Button(ventana, text = "Guardar", command = Guardar(Nombre, nfoto, cortar), font = ("Verdana", 5), height = 6, width = 6).pack()
    ventana.mainloop()
    
def Guardar(Nombre, nfoto, cortar):
    