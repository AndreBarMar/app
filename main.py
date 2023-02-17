from flask import Flask
import pickle


modelo = pickle.load(open('modelo.pkl', 'rb'))


app = Flask(__name__)


@app.route('/')
def home():
    return "API para saber se tem ou não diabetes."


@app.route('/soma/<int:valor>')
def soma(valor):
    return "Resultado: {}".format(valor+5)


@app.route('/predicao/<float:v1>/<float:v2>/<float:v3>/<float:v4>/<float:v5>/<float:v6>')
def predicao(v1, v2, v3, v4, v5, v6):
    resultado = modelo.predict([[v1, v2, v3, v4, v5, v6]])
    return "Classe: {}".format(resultado)


app.run(debug=True)
