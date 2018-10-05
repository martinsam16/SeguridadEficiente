import MySQLdb as demo

BaseDeDatos = demo.connect(host="localhost",user="root",passwd="root",db="_")

cur= BaseDeDatos.cursor()

cur.execute("create table if not exists DesdePython(id int primary key auto_increment, demo varchar(12))")

#cur.execute("insert into DesdePython(demo) values('elfuturo')")
cur.execute("SELECT * FROM _")

print cur.fetchall()

cur.close()
