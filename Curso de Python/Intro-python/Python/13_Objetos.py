class Usuario:
   # El primer argumento, hace referencia a la instancia.
   def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

   def saludo(self):
      print('Hola, mi nombre es ',self.nombre, self.apellido)

usuario = Usuario('Hernan','Franco')

usuario.saludo()
usuario.nombre = 'Gaston'
usuario.saludo()

# Eliminamos la propiedad nombre
del usuario.nombre

# Eliminamos el objeto usuario
del usuario