import mysql.connector

midb = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   password = '',
   database = 'Prueba'
)

cursor = midb.cursor()

# Devuelve un elemento 
cursor.execute('select * from Usuario limit 1')

# Insertamos dato
# sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
# values = ('micorreo@gmail.com' , 'gatomalo', 45)

# Actualizamos un dato
# sql = 'update Usuario set email = %s where id = %s'
# values = ('queti@hotmail.com', 8)

# Para ejecutar una consulta sql. Necesitamos la consulta y los valores
# cursor.execute(sql, values)

# Eliminar Datos
# sql = 'delete from Usuario where id = %s'
# values = (6, ) # Dejar siempre un espacio despues de la coma
# cursor.execute(sql, values)

# fetchall Devuelte todas las instancias que encontro
# fetchone Duvuelve el primer elemento que este encontro
resultado = cursor.fetchall()

# Toma los datos y ejecuta la consulta sql
# midb.commit()
# print(cursor.rowcount)

print(resultado)