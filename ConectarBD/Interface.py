#-*- coding:utf-8 -*-
from tkinter import *
#funciones de procesamiento
def Registrar():
        Registrar = Registrando.get()
#Instancia de la clase Tk
ventana = Tk()
ventana.title('REGISTRAR')

#Variables que almacenarán los datos
ID = IntVar ()
Nombre = StringVar()
Apellidos = StringVar()
DNI = IntVar()
FechaNaci = IntVar()
Direccion = StringVar()
NroCel = IntVar()
genero = IntVar()
genero.set(1)
Foto = StringVar()

#ID
etiqueta_ID = Label(ventana, text='ID:')
entrada_ID = Entry(ventana, textvariable=ID)
etiqueta_ID.grid(row=1, column=1)
entrada_ID.grid(row=1, column=2)
#Nombre
etiqueta_Nombre = Label(ventana, text='Nombre:')
entrada_Nombre = Entry(ventana, textvariable=Nombre)
etiqueta_Nombre.grid(row=2, column=1)
entrada_Nombre.grid(row=2, column=2)

#Apellidos
etiqueta_Apellidos = Label(ventana, text='Apellidos: ')
entrada_Apellidos = Entry(ventana, textvariable=Apellidos)
etiqueta_Apellidos.grid(row=3, column=1)
entrada_Apellidos.grid(row=3, column=2)

#DNI
etiqueta_DNI = Label(ventana, text='DNI: ')
entrada_DNI = Entry(ventana, textvariable=DNI)
etiqueta_DNI.grid(row=4, column=1)
entrada_DNI.grid(row=4, column=2)

#FechaNaci
etiqueta_FechaNaci = Label(ventana, text='Fecha Nacimiento: ')
entrada_FechaNaci = Entry(ventana, textvariable=FechaNaci)
etiqueta_FechaNaci.grid(row=5, column=1)
entrada_FechaNaci.grid(row=5, column=2)

#Direccion 
etiqueta_Direccion  = Label(ventana, text='Direccion : ')
entrada_Direccion = Entry(ventana, textvariable=Direccion )
etiqueta_Direccion .grid(row=6, column=1)
entrada_Direccion .grid(row=6, column=2)

#Numero Cel
etiqueta_NroCel  = Label(ventana, text='Nro Celular : ')
entrada_NroCel = Entry(ventana, textvariable=NroCel)
etiqueta_NroCel .grid(row=7, column=1)
entrada_NroCel .grid(row=7, column=2)


#genero
etiqueta_genero = Label(ventana, text='Genero: ')
entrada_genero_1 = Radiobutton(ventana, text='Masculino', variable=genero, value=1)
entrada_genero_2 = Radiobutton(ventana, text='Femenino', variable=genero, value=2)
etiqueta_genero.grid(row=8, column=1)
entrada_genero_1.grid(row=8, column=2)
entrada_genero_2.grid(row=8, column=3)

#Foto
etiqueta_Foto  = Label(ventana, text='Foto : ')
entrada_Foto = Entry(ventana, textvariable=Foto)
etiqueta_Foto .grid(row=9, column=1)
entrada_Foto .grid(row=9, column=2)

#boton
boton = Button(ventana, text='Registrar', command=Registrar, width=20)
boton.grid(row=12, column=3)

#ejecución de ventana
ventana.mainloop()
