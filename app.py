from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Inicio</h1>"

if __name__ == '__main__':
    app.run(debug=True)