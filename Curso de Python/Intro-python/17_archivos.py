

# Abrimos el archivo
# r = Leer
# a = Agrega datos al final
# w = Modifica el archivo en su totalidad. Sino existe el archivo lo crea
# x = Crea un archivo
#c = open('archivo.txt', 'w')

# read() Leemos el archivo
# readline() Lee una linea hasta encontrar un espacio en blanco
#print(c.readline())

#for x in c:
#	print(x)

#c.write('\nAgregamos una nueva linea a nuestro archivo!')

# Cierra el archivo
#c.close()

#x = open('archivo.txt')

#print(x.read())

# Nos permite eliminar archivos o carpetas
import os 

# Preguntamos si el archivo existe
if os.path.exists('archivo.txt'):
	# Elimina el archivo
	os.remove('archivo.txt')
else:
	print('El archivo no existe!')

# Elimina la carpeta o directorio
os.rmdir('miCarpeta')