from flask import Flask, request, url_for, redirect
app = Flask(__name__)

# Nos permite llamar a la ruta desde el explorar web
@app.route('/')
def index():
   return 'Hola Mundo'

#<> Va el nombre de una variable. Que mas adelante haremos referencia en el codigo
#<int:id> Forzamos que el dato sea entero
#methods=[] Ingresamos el metodo
#request.method == 'metodo' Una sola funcion maneje varios metodos
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
   if request.method == 'GET':
      return 'ID '+ post_id
   else:
      return 'Este es otro metodo'

# url_for sirve para crear una url
@app.route('/lele', methods=['POST', 'GET'])
def lele():
   #Siempre debe tener un return el redirect que este sirve para redireccionar
   return redirect(url_for('lala', post_id=2))
   # print(request.form)
   # print(request.form['llave1'])
   return 'lele'

