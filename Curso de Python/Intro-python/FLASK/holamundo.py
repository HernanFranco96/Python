from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)
import mysql.connector

midb = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   password = '',
   database = 'Prueba'
)

#generamos el cursor
cursor = midb.cursor(dictionary=True)

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
   cursor.execute("select * from Usuario")
   usuarios = cursor.fetchall()
   print(usuarios)
   # abort Detiene la ejecucion de nuestra funcion y devuelve un mensaje de error
   # abort(401)
   # Siempre debe tener un return el redirect que este sirve para redireccionar
   # return redirect(url_for('lala', post_id=2))
   # print(request.form)
   # print(request.form['llave1'])
   # Le devolvemos al usuario una pagina web
   # return render_template('lele.html')
   # Podemos devovler un diccionario. Objeto JSON
   # return {
   #    "username" : 'Hernan Franco',
   #    "email" : 'hernan@gmail.com'
   # }

   #Le entregamos a la platilla lele.html los usuarios de la base de datos
   return render_template("lele.html", usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
   #mensaje es una variable que pasamos a traves de nuestra funcion render a la pagina home.html
   return render_template('home.html', mensaje='Hola Mundo')

# Guardamos dato en la base de datos
@app.route('/crear', methods=['POST', 'GET'])
def crear():
   if request.method == "POST":
      email = request.form['email']
      username = request.form['username']
      edad = request.form['edad']
      sql = "insert into Usuario (email, username, edad) values (%s, %s, %s)"
      values = (email, username, edad)
      cursor.execute(sql, values)
      midb.commit()
      return redirect(url_for('lele'))
   return render_template('crear.html')