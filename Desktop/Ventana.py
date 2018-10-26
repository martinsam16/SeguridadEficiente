import Tkinter as tkint, os,shutil as shu

def CrearCarpeta(nombre):
  os.mkdir("./img/"+nombre)
 
def EliminarCarpeta(nombre):
  shu.rmtree("./img"+nombre)
  
def IngresarDatos():
  
  
class IniciarVentana(imagen,nombre):
    root=tkint.Tk()
    btn=tkint.Button(root,text="Registrar",command=IngresarDatos)
    btn.pack()
    root.title("Principal")
    root.mainloop()
