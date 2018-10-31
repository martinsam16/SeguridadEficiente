#-*- coding:utf-8 -*-
from tkinter import *

#funciones de procesamiento
def Resetear():
	Resetear=clear.get
def Entrenar():
	Entrenar=entremaiento
	
#Instancia de la clase Tk
ventana = Tk()
ventana.title('Entrenador')

#Variables que almacenarán los datos
URL = StringVar()

#peso
etiqueta_URL = Label(ventana, text='URL:')
entrada_URL = Entry(ventana, textvariable=URL)
etiqueta_URL.grid(row=1, column=1)
entrada_URL.grid(row=1, column=2)
#boton
boton = Button(ventana, text='Resetear', command=Resetear, width=20)
boton.grid(row=4, column=3)
boton = Button(ventana, text='Entrenar', command=Entrenar, width=20)
boton.grid(row=4, column=2)

#ejecución de ventana
ventana.mainloop()
