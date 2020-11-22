from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def index(name="Hernán"):
   age = 19
   my_list = [1,2,3,4]
   return render_template('index.html', name=name,age=age,my_list=my_list)

if __name__ == "__main__":
   app.run(debug=True, port=8000)