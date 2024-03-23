import os
import threading

from flask import Flask, render_template, jsonify
from pyngrok import ngrok
import json
import random as r

app = Flask(__name__)

port = "5000"

# Definindo o authtoken do ngrok
authtoken = "seu_token"  # Substitua "SEU_AUTHTOKEN" pelo token que você copiou

# Configure o authtoken
ngrok.set_auth_token(authtoken)

# Abrindo o tunel http NGROK
public_url = ngrok.connect(port).public_url

# Imprimindo a url do tunnel no console, pois caso contrario seria perdida na execucao
print(f"* ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

# Atualizando todas as URL Base para uso publico do NGROK
app.config["BASE_URL"] = public_url

# Dados a serem inseridos no arquivo JSON
d = [
    {"Number": 1, "Name": "Mahesh", "Age": 25, "City": "Bangalore", "Country": "India"},
    {"Number": 2, "Name": "Alex", "Age": 26, "City": "London", "Country": "UK"},
    {"Number": 3, "Name": "David", "Age": 27, "City": "San Francisco", "Country": "USA"},
    {"Number": 4, "Name": "John", "Age": 28, "City": "Toronto", "Country": "Canada"},
    {"Number": 5, "Name": "Chris", "Age": 29, "City": "Paris", "Country": "France"}
]

@app.route('/')
def home():
    """
    The entire line below must be written in a single line.
    """
    return "<marquee><h3> TO CHECK INPUT ADD '/input' TO THE URL AND TO CHECK OUTPUT ADD '/output' TO THE URL.</h3></marquee>"


@app.route("/input") # Code to assign Input URL in our app to function input.
def input():
    return jsonify(d) # "d" is the dictionary we defined


#@app.route('/output', methods=['GET','POST']) #output page
#def predjson():
#    pred = r.choice(["positive", "negative"])
#
#    for person in d:
#        person["prediction"] = pred
#    return jsonify(d)

if __name__ == '__main__':
    app.run()