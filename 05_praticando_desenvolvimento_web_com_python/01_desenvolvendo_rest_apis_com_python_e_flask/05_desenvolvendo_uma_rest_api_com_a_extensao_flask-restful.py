"""
    REST vc RESTful

    REST é um estilo arquitetônico, um modelo para se seguir ao
    desenvolver APIs.

    RESTful é um serviço web que utiliza esse paradigma. É utilizado
    para definir aplicações que implementam webservices que utilizam
    a arquitetura REST.

    Podemos dizer que uma aplicação web que segue a arquitetura REST,
    ela é RESTful, ou seja, tem a capacidade de seguir a arquitetura
    REST.
"""

"""
    Flask-RESTful

    - É uma extensão do Flask que adiciona suporte para construção
    rápida de REST APIs.

    - O uso do Flask-RESTful acaba incentivando as práticas recomendadas
    para a arquitetura REST com uma configuração leve.
"""

"""
    Exemplo:

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class HelloWordl(Resource):
    def get(self):
        return {'hello': 'world'}
    
api.add_resource(HelloWordl, '/')

if __name__ == '__main__':
    app.run(debug=True)

"""

from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
import json
from habilidades import Habilidades

app = Flask(__name__)

api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Roberth',
        'habilidades': ['Python', 'Flask', 'Redes']
    },
    {
        'id':'1',
        'nome':'Larissa',
        'habilidades':['Bolo', 'Lasanha']
    }
]


# Devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'error', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}
        return response
    
    def put(self, id):
        dados = request.json
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':"registro excluido"}


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = request.json
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')

api.add_resource(ListaDesenvolvedores, '/dev')

api.add_resource(Habilidades, '/habilidades')


if __name__ == '__main__':
    app.run(debug=True)