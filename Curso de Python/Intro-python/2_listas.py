
lista = ["Boca", "Juniors", "Mundial"]
# Copia la lista 1 y la pega en la dos
lista2 = lista.copy()
# Agregar datos a nuestra lista
lista.append("Zspacial")

# Elimina todos los elementos de nuestra lista
# lista.clear()

# .count() Nos indica cuantas veces se muestra el valor dentro de la lista
# print(lista, lista2.count(3))
# len Indica la cantidad de elementos que tiene la lista
# print(len(lista), len(lista2))

largoLista = len(lista)
largoLista2 = len(lista2)

#print(largoLista, largoLista2)

# Mostramos el indice indicado entre corchetes
# print(lista[2])

# pop() elimina el ultimo elemento de la lista
# lista.pop()

# remove() elimina el elemento indicado
# lista.remove("Juniors")

# Cambia el orden de la lista
# lista.reverse()

# Ordena la lista de menor a mayor si los datos son del mismo tipo
lista.sort()
print(lista)