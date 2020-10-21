
# Multiplicar dos numeros sin usar el simbolo de multiplicacion
a = 4
b = 8
resultado = 0

for x in range(b):
    resultado += b

#print(resultado)

# Ingresar nombre y apellido e imprimirlo al reves

nombre = 'Hernan'  
apellido = 'Franco'

concatenacion = nombre + ' ' + apellido

# Da vuelta un string 
#print(concatenacion[::-1])

# Escribir una funcion que encuentre el elemento menor en una lista

lista = [5, 3, 4, 2, -10, 10]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

#print(menor)

# Escribir una funcion que devuelva el volumen de una esfera por su radio 
# 4/3 * pi * r ** 3

# ** Es elevar
def calcularVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calcularVolumen(6)
#print(resultado)

# Escribir una funcion que indique si el usuario es mayor de edad

def esMayor(e):
    return e.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

user = Usuario(15)
user2 = Usuario(22)

resultado1 = esMayor(user)
resultado2 = esMayor(user2)

#print(resultado1, resultado2)

# Escribir una funcion que indique si un numero es par o impar

def valNumero(n):
    return 'Par' if n % 2 == 0 else 'Impar'

#print(valNumero(8))

# Escribir una funcion que indique cuantas vocales tiene una palabra

vocales = 0
palabra = 'hernanfrancoahrechua'

for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

#print(vocales)

# Escribir una aplicacion que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelta la suma de los numeros ingresados

lista = []
#print('Ingrese numeros y salir escriba "basta" ')
#while True:
    #valor = input('Ingrese valor: ')   
    #if valor == 'basta':
    #    break
    #else:
    #    try:
    #        valor = int(valor)
    #        lista.append(valor)
    #    except:
    #        print('Dato invalido')
    #        exit()

resultado = 0
for x in lista:
    resultado += x
#print(resultado)

#Escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregar(nombre, apellido):
    c = open('archivo.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregar('Hernan','Franco')