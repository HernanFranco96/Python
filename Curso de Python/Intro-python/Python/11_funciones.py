
def miFuncion():
   print('Mi primera funcion')

#miFuncion()

#Muestra una lista
def imprimeDato(*nombre):
   print('El nombre completo es: ',nombre)

#imprimeDato('Hernan','Franco','Boca')

def nombreCompleto(apellido,nombre):
   print(nombre,apellido)

#nombreCompleto(nombre='Hernan',apellido='Franco')

def nombreCompletoDos(**kwargs):
   print(kwargs['nombre'], kwargs['apellido'])


#nombreCompletoDos(nombre='Hernan',apellido='Franco')

def miFuncionDos(argumento = 'Hernan'):
   print(argumento)

# Al pasar un valor por predeterminado al ser llamado sin argumentos se imprimira el argumento predeterminado
#miFuncionDos('Franco')
#miFuncionDos()

def miFuncionLista(lista):
   for i in lista:
      print(i)

#miFuncionLista(['Boca','Juniors'])

def concatenaNombres(lista):
   i = ''
   for el in lista:
      i = i + el + ' '
   return i

nombres = concatenaNombres(['Boca','Juniors'])
print(nombres)