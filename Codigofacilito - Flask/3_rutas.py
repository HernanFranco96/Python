from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
   return 'Mensaje'

@app.route('/params')
def params():
   # Recibe el valor del primer parametro params1 o un mensaje si no recibe ningun parametro
   param = request.args.get('params1', 'no contiene este parametro')
   param2 = request.args.get('params2', 'no contiene este parametro')
   return 'El parametro es: {}, {}'.format(param, param2)

if __name__ == "__main__":
   app.run(debug=True, port=8000)