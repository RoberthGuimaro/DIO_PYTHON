from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id':id, 'nome':'Roberth', 'profissao':'dev'})

#@app.route('/soma/<int:valor_1>/<int:valor_2>/')
#def soma(valor_1, valor_2):
#    return jsonify({'soma': valor_1 + valor_2})


@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data) 
        print(dados)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10+10
    return jsonify({'soma':total})

if __name__ == '__main__':
    app.run(debug=True)