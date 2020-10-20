class Usuario:
   # El primer argumento, hace referencia a la instancia.
   def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

   def saludo(self):
      print('Hola, mi nombre es ',self.nombre, self.apellido)

#Indicamos entre parentesis que hereda de Usuario
class Admin(Usuario):
   def superSaludo(self):
      print('Hola, me llamo ', self.nombre + ' y soy administrador')

admin = Admin('Hernan','Franco')
admin.saludo()
admin.superSaludo() 
