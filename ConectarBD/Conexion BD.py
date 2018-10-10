import  mysql.connector
def Conectar ():
    global cnn
    global cursor
    server = '127.0.0.1' 
    database = 'Seguridad_Eficiente' 
    username = 'root' 
    password = 'tucontraseña' 
    cnn = pypyodbc.connect('DRIVER={ODBC Driver 17 for MySQL};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    print("Conexion establecida con exito")
def agregar ():
    CantidadUsuario=int(input("Cuantos Usuarios va a ingresar:"))
    x=0
    while x< CantidadAlumnos:
        ID = input("INT AUTO_INCREMENT ")
        Nombre = input("Ingrese el nombre del usuario: ")
        Apellido = input("Ingrese el apellido del usuario: ")
        DNI= input("Ingrese el DNI del alumno: ")
        FechadeNacimiento = input("Ingrese Fecha de Nacimiento del Usuario : ")
        Direccion = input("Ingrese Direccion del Usuario : ")
        Numerodecelular = input("Ingrese Numero de celular el Usuario : ")
        Genero = input("Ingrese Genero del Usuario : ")
        Foto = input("Ingrese la  Foto de la Usuario : ")
        PuntosFaciales  = input("Ingrese Puntos Faciales del aUsuario : ")
        cursor = cnn.cursor()
        sqlcmd = ("INSERT INTO Usuarios (ID,Nombre,Apellido,DNI,FechadeNacimiento,Direccion,Numerodecelular,Genero,Foto,PuntosFaciales)"
                  "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%\
                 (ID,Nombre,Apellido,DNI,FechadeNacimiento,Direccion,Numerodecelular,Genero,Foto,PuntosFaciales ))
        x = x + 1
        cursor.execute(sqlcmd)
        cnn.commit()
        print("Registro insertado correctamente")
def buscar ():
    cursor = cnn.cursor()
    ID =int(input("Ingrese el IDUSUARIO: "))
    ConsultaID = "SELECT * FROM Usuarios WHERE ID="+ str(ID)
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
    op = input("Ingrese la opcion que desea realizar  del 1 al 3: ")
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
  
  
