tupla = ("Hola", "Mundo", "somos", "Tupla")

# count() Indica la cantidad de veces que se repite el valor
# cantidadPalabra = tupla.count("Hola")

# index indica la posicion del valor indicado
#index = tupla.index("Mundo")

# Las tuplas no pueden modificarse
# Debemos transformar una tupla en lista
listaDeTupla = list(tupla)
listaDeTupla.append("lalala")

print(listaDeTupla)

