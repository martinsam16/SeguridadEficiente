import  MySQLdb
def Conectar ():
    global conn
    global cursor
    server = 'localhost' 
    database = 'Seguridad_Eficiente' 
    username = 'root' 
    password = 'root' 
    conn = MySQLdb.connect('DRIVER={ODBC Driver  for MySQL server};SERVER='+localhost+';DATABASE='+Seguridad_Eficiente+';UID='+root+';PWD='+ root)
    print("Conexion establecida con exito")
def agregar ():
    CantidadUsuario=int(raw_input("Cuantos Usuarios va a ingresar:"))
    x=0
    while x< CantidadUsuario:
        ID = int(raw_input("Ingrese el ID de Usuario: "))
        Nombre = raw_input("Ingrese el nombre del usuario: ")
        Apellido = raw_input("Ingrese el apellido del usuario: ")
        DNI= int(raw_input("Ingrese el DNI del alumno: "))
        FechadeNacimiento = (raw_input("Ingrese Fecha de Nacimiento del Usuario : "))
        Direccion = raw_input("Ingrese Direccion del Usuario : ")
        Numerodecelular = int(raw_input("Ingrese Numero de celular el Usuario : "))
        Genero = raw_input("Ingrese Genero del Usuario : ")
        Foto = raw_input("Ingrese la  Foto de la Usuario : ")
        PuntosFaciales  = raw_input("Ingrese Puntos Faciales del Usuario : ")
        cursor = cnn.cursor()
        sql = ("INSERT INTO Usuarios (ID,Nombre,Apellido,DNI,FechadeNacimiento,Direccion,Numerodecelular,Genero,Foto,PuntosFaciales)"
                  "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%\
                 (ID,Nombre,Apellido,DNI,FechadeNacimiento,Direccion,Numerodecelular,Genero,Foto,PuntosFaciales ))
        x = x + 1
        cursor.execute(sql)
        conn.commit()
        print("Registro insertado correctamente")
def buscar ():
    cursor = conn.cursor()
    ID =int(raw_input("Ingrese el ID Usuario: "))
    ConsultaID = "SELECT * FROM Usuario WHERE ID="+ str(ID)
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
            print ("PuntosFaciales Usuario: ",registro[9])

def menu():
    print ("MENU DE OPCIONES")
    print ("""\t\t\t1. Conectar la Base De datos\n
               \t\t2. Agregar datos a la tabla\n
               \t\t3. Buscar datos de la base de datos""")
    op = raw_input("Ingrese la opcion que desea realizar  del 1 al 3: ")
    if op == "1":
        Conectar ()
        menu()
    if op =="2":
        agregar()
        menu()
    if op=="3":
        buscar()
        menu()
        
menu()
 

