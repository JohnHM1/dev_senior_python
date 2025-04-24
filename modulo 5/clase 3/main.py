import mysql.connector as mysql

#configuraciones de conexion
conexion = mysql.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "conexion",
    port = 3306
)

#Verificar si la conexion fue exitosa
if conexion.is_connected():
    print("Conexion exitosa")

####Ejecutar una consulta SQL
cursor = conexion.cursor()
# cursor.execute("create table usuarios ("
#                 "id int auto_increment primary key,"
#                 "nombre varchar(50),"
#                 "apellido varchar(50),"
#                 "edad int"
#                 ")")

###Insertar datos en la tabla
# query = "insert into usuarios (nombre, apellido, edad) values (%s, %s, %s)"
# valores = ("Juan", "Perez", 25)
# cursor.execute(query, valores)
# conexion.commit()

# print(f'Fila insertada con exito, id: {cursor.rowcount}')


###Actualizar datos en la tabla
# query = "update usuarios set nombre = %s where id = %s"
# valores = ("Pedro", 1)
# cursor.execute(query, valores)
# conexion.commit()#Guardar cambios


##Eliminar datos en la tabla
query = "delete from usuarios where id = %s"
valores = (1,)
cursor.execute(query, valores)
conexion.commit()#Guardar cambios    





###Mostrar datos de la tabla
cursor.execute("select * from usuarios") #Ejecutar consulta
usuarios = cursor.fetchall() #Obtener todos los registros
for usuario in usuarios:
    print(usuario)
print(f'Fila actualizada con exito, id: {cursor.rowcount}')


###cerrar la conexion
conexion.close()
print("Conexion cerrada")
