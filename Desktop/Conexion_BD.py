import mysql.connector
	
def Conectar ():
    global cnn
    global cursor
    try:
        cnn = mysql.connector.connect(host="localhost",user="root",passwd="root",db="Seguridad_Eficiente")
        cursor=cnn.cursor()
        print ("Conexión Exitosa! "+cnn.get_server_info())
        return True
    except Exception as e:
        print (e)
        return False
        
      
def agregar (ID,NomUser,ApellUser,DNIUser,FechNacUSer,DirecUser,NroCellUser,GenrUser,FotoUser):
    try:
        cursor = cnn.cursor()
        sql = ("INSERT INTO USUARIO (CODUSER,NomUser,ApellUser,DNIUser,FechNacUSer,DirecUser,NroCellUser,GenrUser,FotoUser)"
                "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%\
                    (ID,NomUser,ApellUser,DNIUser,FechNacUSer,DirecUser,NroCellUser,GenrUser,FotoUser,))
        cursor.execute(sql)
        cnn.commit()
        print("Registro insertado correctamente")
    except Exception as e:
        print (e)
        pass

"""    
def buscar ():
    cursor = cnn.cursor()
    ID =int(input("Ingrese el ID Usuario: "))
    ConsultaID = "SELECT * FROM USUARIO WHERE ID="+ str(ID)
    cursor.execute(ConsultaID)

    DatoID= cursor.fetchall()
    for x in range (1):
        for registro in DatoID:
            print ("Numero de ID: ",registro[0])
            print ("Nombre del Usuario: ",registro[1])
            print ("Apellido del Usuario: ",registro[2])
            print ("DNI del Usuario: ",registro[3])
            print ("FechadeNacimiento Usuario: ",registro[4])
            print ("Direccion Usuario: ",registro[5])
            print ("Numerodecelular Usuario: ",registro[6])
            print ("Genero Usuario: ",registro[7])
            print ("Foto Usuario: ",registro[8])
            
def cerrar ():
    exit()
#def entrenar ():
   # import Entrenar
"""