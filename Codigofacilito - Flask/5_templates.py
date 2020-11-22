from flask import Flask, render_template

#template_folder="prueba_template"
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True, port=8000)
