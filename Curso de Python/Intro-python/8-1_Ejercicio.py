
primero = input('Ingrese primer numero: ')

try:
   primero = int(primero)
except:
   primero = "lalala"

if primero == 'lalala':
   print('El valor ingresado no es un entero')
   exit()


segundo = input('Ingrese segundo numero: ')

try:
   segundo = int(segundo)
except:
   segundo = "lelele"

if segundo == 'lelele':
   print('El valor ingresado no es un entero')
   exit()

simbolo = input('Ingrese operacion: ')

if simbolo == '+':
   print('Suma: ', primero+segundo)
elif simbolo == '-':
   print('Resta: ', primero-segundo)
elif simbolo == '*':
   print('Multiplicacion: ', primero*segundo)
elif simbolo == '/':
   print('division: ', primero/segundo)
else:
   print('El simbolo ingresado no es valido!')


