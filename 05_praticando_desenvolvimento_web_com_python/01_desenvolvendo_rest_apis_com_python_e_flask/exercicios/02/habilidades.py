"""
    Exercício para praticar

    - Acrescentar na API de habilidade (módulo habilidades) os métodos
    PUT, POST e DELETE.

    - O método POST deverá inserir uma habilidade nova na lista.

    - O método PUT a partir de um ID (identificador da posição)
    deverá alterar o nome da habilidade que está naquela posição.

    - O método DELETE deverá deletar uma habilidade que esteja na
    posição informada na requisição.

    - Incluir validação no app-restful para verificar se habilidades
    informadas existem na lista habilidades.
"""

from flask_restful import Resource
from flask import request

# Lista de habilidades
lista_habilidades = ['Python', 'Java', 'Flask', 'Django']

# Class Habilidades que fara as modificacoes e retornos da lista_habiilidades
class Habilidades(Resource):
    # Retorna a lista de habilidades
    def get(self):
        return lista_habilidades
    
    # Insere uma nova habilidade na lista
    def post(self):
        dados = request.json
        # Checa se habilidade ja existe na lista
        if dados in lista_habilidades:
            return {'message':'Habilidade ja existente'}
        
        else:
            # Inclui habilidade na lista habilidades
            lista_habilidades.append(dados)
            return dados
    
class SubstituiHabilidade(Resource):
    
    def put(self, id):
        dados = request.json
        # Checa se o tamanho do id e maior que zero e menor que o tamanho da lista
        # substitui a habilidade antiga pela nova
        if 0 <= id < len(lista_habilidades):
            habilidade_antiga = lista_habilidades[id]
            lista_habilidades[id] = dados
            return {'habilidade antiga':habilidade_antiga, 'habilidade nova': lista_habilidades[id]}
        
        # Caso o id seja maior que a lista retorna um erro
        else:
            return {'message':'ID maior que o numero de itens na lista'}

    def delete(self, id):
        # Checa se o tamanho do id e maior que zero e menor que o tamanho da lista
        # Apaga a habilidade com id especificado
        if 0 <= id < len(lista_habilidades):
            habilidade = lista_habilidades[id]
            lista_habilidades.pop(id)
            message = f"Habilidade {habilidade} foi apagada"
            return {'messsage':message}
        
        # Caso o id seja maior que a lista retorna um erro
        else:
            return {'message':'ID maior que o numero de itens na lista'}