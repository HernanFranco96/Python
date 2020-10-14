class Usuario:
   def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

usuario = Usuario('Hernan','Franco')
#usuario2 = Usuario('')

print(usuario.nombre,usuario.apellido)
