#from modulos import saludo, mascotas 
import modulos as xs 
from camelcase import CamelCase 

print(xs.mascotas)
xs.saludo('Nicolas')

#print('mascotas')
#print(saludo('Hernan'))


c = CamelCase()
s = 'Esta horacion necesita CamelCase'

#Todas las palabras comienzan en mayusculas.
camelcase = c.hump(s)
print(camelcase)

# pip install = Instala un modulo
# pip list = Lista los modulos
# pip unistall = Desistala un modulo
