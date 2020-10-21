
diccionario = {
   "nombre": "Simon",
   "raza": "Persa",
   "edad": 5
}

#print(diccionario)
#print(diccionario['nombre'])
#print(diccionario['raza'])

# Con get accedemos a un elemento dentro del diccionario
#print(diccionario.get('nombre'))

# Cambiamos el valor de nombre
# diccionario['nombre'] = "Carlos"

# len() indica la cantidad de elementos de un diccionario
# print(len(diccionario))

diccionario['ladra'] = 'Si'

# pop() elimina el valor indicado
# diccionario.pop('ladra')

# popitem() elimina el ultimo valor 
# diccionario.popitem()

# copy() hace una copia del direccionario original
# copiaPerro = diccionario.copy()

# Pasando a la funcion dict retorna una copia del diccionario
copiaPerro = dict(diccionario)

# Usando la palabra reservada del elimina el valor indicado
# del diccionario['ladra']

# clear() Elimina todos los valores que tiene mi diccionario
diccionario.clear()
# print(diccionario, copiaPerro)

###########################################################

tomi = {
   "nombre": "Tomi",
   "edad": 12
}
eva = {
   "nombre": "Eva",
   "edad": 8
}
# Diccionario anidado
perros = {
   "Tomi": tomi,
   "Eva": eva
}

print(perros)

peces = dict(nombre="Betta", edad=3)

print(peces)