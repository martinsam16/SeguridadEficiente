import mysql.connector
	
def Conectar ():
    global cnn
    global cursor
    server = 'localhost' 
    database = 'Seguridad_Eficiente' 
    username = 'root' 
    password = 'root' 
    cnn = mysql.connector.connect(host="localhost",user="root",passwd="root",db="Seguridad_Eficiente")
    print("Conexion establecida con exito")
    
def agregar ():
    CantidadUSUARIO=int(input("Cuantos Usuarios va a ingresar:"))
    x=0
    while x< CantidadUSUARIO:
        ID = int(input("Ingrese el ID de Usuario: "))
        NomUser = input("Ingrese el nombre del usuario: ")
        ApellUser = input("Ingrese el apellido del usuario: ")
        DNIUser= int(input("Ingrese el DNI del alumno: "))
        FechNacUSer = (input("Ingrese Fecha de Nacimiento del Usuario : "))
        DirecUser = input("Ingrese Direccion del Usuario : ")
        NroCellUser = int(input("Ingrese Numero de celular el Usuario : "))
        GenrUser = input("Ingrese Genero del Usuario : ")
        FotoUser = input("Ingrese la  Foto de la Usuario : ")
        cursor = cnn.cursor()
        sql = ("INSERT INTO USUARIO (ID,NomUser,ApellUser,DNIUser,FechNacUSer,DirecUser,NroCellUser,GenrUser,FotoUser)"
                  "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%\
                 (ID,NomUser,ApellUser,DNIUser,FechNacUSer,DirecUser,NroCellUser,GenrUser,FotoUser,))
        x = x + 1
        cursor.execute(sql)
        cnn.commit()
        print("Registro insertado correctamente")
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
    
def menu():
    print ("MENU DE OPCIONES")
    print ("""\t\t\t1. Conectar la Base De datos\n
                \t\t2. Agregar datos a la tabla\n
                \t\t3. Buscar datos de la base de datos
                \t\t4. Cerrar Base De datos\n""")
    
    op = input("Ingrese la opcion que desea realizar  del 1 al 4: ")
    if op == "0":
        Crear()
        menu()
    if op == "1":
        Conectar ()
        menu()
    if op =="2":
        agregar()
        menu()
    if op =="3":
        buscar()
        menu()
    if op == "4":
        cerrar()
menu()



