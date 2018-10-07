import MySQLdb as demo

BaseDeDatos = demo.connect(host="localhost",user="root",passwd="root",db="Demo")

cur= BaseDeDatos.cursor()

cur.execute("create table if not exists TablaDemo(id int primary key auto_increment, Nombre varchar(12))")

#cur.execute("insert into DesdePython(demo) values('elfuturo')")
cur.execute("SELECT * FROM TablaDemo")

print cur.fetchall()

cur.close()