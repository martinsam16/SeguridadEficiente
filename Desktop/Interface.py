#-*- coding:utf-8 -*-
from tkinter import *
import Conexion_BD,Entrenar as ent, Seguridad_Eficiente as seg

#Instancia de la clase Tk
ventana = Tk()
ventana.title('INICIO')

ID=0
Nombre=""
Apellidos=""
DNI=""
FechaNaci=""
Direccion=""
NroCel=""
genero=""
Foto="./carpeta//"
a=""

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
etiqueta_genero = Label(ventana, text='Genero (M-F): ')
entrada_genero = Entry(ventana, textvariable=genero)
etiqueta_genero.grid(row=8, column=1)
entrada_genero.grid(row=8, column=2)

#Foto
etiqueta_Foto  = Label(ventana, text='Ruta Foto : ')
entrada_Foto = Entry(ventana, textvariable=Foto)
etiqueta_Foto .grid(row=9, column=1)
entrada_Foto .grid(row=9, column=2)

#Funcion del btn que insertará registros en la DB
def Registrar():
        Registrar = Conexion_BD.conectar()
        if (Registrar):
                Conexion_BD.agregar(entrada_ID.get(),entrada_Nombre.get(),entrada_Apellidos.get(),entrada_DNI.get(),entrada_FechaNaci.get(),entrada_Direccion.get(),entrada_NroCel.get(),entrada_genero.get(),entrada_Foto.get())
        else:
                pass

def Entrenar():
        a = ent.Entrenamiento()
        print (a)

def MostrarSegEfi():
        seg.IniciarIdentificacion()

btnReg = Button(ventana, text='Registrar', command=Registrar, width=20).grid(row=12, column=3)
btnSeg= Button(ventana, text='Iniciar',command=MostrarSegEfi,width=20).grid(row=12, column=1)
btnEntrenar= Button(ventana, text='Entrenar', command=Entrenar, width=20).grid(row=12, column=2)

ventana.mainloop()
