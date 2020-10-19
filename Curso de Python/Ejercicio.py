
i = 0
index = True
alumnos = []
listar = False


while(index):

   n = input('Ingrese nombre: ')
   e = input('Ingrese edad: ')

   try:
      n = str(n)
      e = int(e)
   except():
      print('Haz ingresado un valor incorrecto.')
      index = False
      exit()

   alumnos.append(dict(nombre=n, edad=e))
   i += 1

   respuesta = input('Desea ingresar otro usuario?\nsi o no? ')

   if(respuesta == 'si'):
      continue
   elif(respuesta == 'no'):
      index = False
      listar = True
   else:
      print('La respuesta ingresada no es correcta.')
      exit()

def listarAlumnos(alumnos):
   nombres = ''
   for a in alumnos:
      nombres += a['nombre'] + ', '
   return nombres

if(listar):
   print('Alumnos: ', listarAlumnos(alumnos) + '- Cantidad de alumnos: ', i)

