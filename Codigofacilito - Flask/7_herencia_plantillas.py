from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   name = 'Eduardo'
   return render_template('7_index.html', name=name)

@app.route('/client')
def client():
   list_name = ['Eduardo','Hernan','Aylen']
   return render_template('7_client.html', lista=list_name)


if __name__ == "__main__":
   app.run(debug=True, port=8000)