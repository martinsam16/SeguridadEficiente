import Tkinter as tk, os,shutil as shu

def CrearCarpeta(nombre):
  os.mkdir("./img/"+nombre)
 
def EliminarCarpeta(nombre):
  shu.rmtree("./img"+nombre)
