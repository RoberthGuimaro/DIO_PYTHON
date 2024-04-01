from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask import request
from flask_httpauth import HTTPBasicAuth
from models import Pessoas
from models import Atividades
from models import Usuarios


auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USUARIOS = {
#    'roberth':'123'
#}

#@auth.verify_password
#def verificacao(login, password):
#    print('Validando usuario')
#    print(USUARIOS.get(login) == password)
#    if not (login and password):
#        return False
#    
#    return USUARIOS.get(login) == password

@auth.verify_password
def verificacao(login, password):
    if not (login and password):
        return False
    
    return Usuarios.query.filter_by(login=login, password=password).first()

class Pessoa(Resource):
    @auth.login_required
    def get(self, name):
        try:
            pessoa = Pessoas.query.filter_by(name=name).first()
            reponse = {
                'name': pessoa.name,
                'age': pessoa.age,
                'id': pessoa.id
            }
        except AttributeError:
            reponse = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return reponse
    
    def put(self, name):
        pessoa = Pessoas.query.filter_by(name=name).first()
        dados = request.json
        if 'name' in dados:
            pessoa.name = dados['name']
        if 'age' in dados:
            pessoa.age = dados['age']

        pessoa.save()
        response = {
            'id':pessoa.id,
            'name':pessoa.name,
            'idade':pessoa.age
        }
        
        return response

    def delete(self, name):
        pessoa = Pessoas.query.filter_by(name=name).first()
        mensagem = f'Pessoa {pessoa.name} excluida com sucesso.'
        pessoa.delete()
        return {'status':'Sucesso', 'mensagem': mensagem}
    
class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'name': i.name, 'age':i.age} for i in pessoas]
        return response
    
    def post():
        dados = request.json
        pessoa = Pessoas(name=dados['name'], idade=dados['age'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'name':pessoa.name,
            'age':pessoa.age
        }
        return response
    
class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'name': i.name, 'pessoa':i.pessoa.name} for i in atividades]
        return response
    
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(name=dados['pessoa']).firts()
        atividade = Atividades(name=dados['name'], pessoa=pessoa)
        atividade.save()
        responde = {
            'pessoa': atividade.pessoa.nome,
            'name': atividade.name,
            'id': atividade.id
        }
    
api.add_resource(Pessoa, '/pessoa/<string:name>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')
if __name__ == '__main__':
    app.run(debug=True)