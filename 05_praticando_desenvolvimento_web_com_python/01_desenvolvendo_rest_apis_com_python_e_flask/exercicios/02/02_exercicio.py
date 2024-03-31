"""
    Exercício para praticar

    - Acrescentar na API de habilidade (módulo habilidades) os métodos
    PUT, POST e DELETE.

    - O método POST deverá inserir uma habilidade nova na lista.

    - O método PUT a partir de um ID (identificador da posição)
    deverá alterar o nome da habilidade que está naquela posição.

    - O método DELETE deverá deletar uma habilidade que estja na
    posição informada na requisição.

    - Incluir validação no app-restful para verificar se habilidades
    informadas existem na lista habilidades.
"""

from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
import json
from habilidades import Habilidades
from habilidades import SubstituiHabilidade

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

api.add_resource(SubstituiHabilidade, '/habilidades/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)