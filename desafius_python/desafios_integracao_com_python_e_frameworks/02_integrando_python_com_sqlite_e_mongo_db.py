""" Desafio 01 - Integrando Python com SQLite e MongoDB
        Parte 01 - Implementando um Banco de Dados Relacional com SQLAlchemy
        
        Objetivo: Neste desafio você irá implementar uma API de integração com SQLite
        com base em um esquema relacional disponibilizado. Sendo assim, utilize o esquema
        dentro do contexto de cliente e conta para criar as classes  de sua API. Essas
        classes irão representar as tabelas do banco de dados relacional dentro da aplicação.

        Entregável: 
            - Aplicação com a definição do esquema por meio das classes usando SQLAlchemy
            - Inserção de um conjunto de dados mínimo para manipulação das informações
            - Execução de métodos de recuperação de dados via SQLAlchemy

        Parte 02 - Implementando um Banco de Dados NoSQL com Pymongo

        Objetivo: Você irá implementar um banco NoSQL com MongoDB para fornecer uma visão
        agregada do modelo relacional. Sendo assim, as informações de cliente e contas
        existentes estão contidas dentro de documentos de acordo com cliente.

        Execute as operações:
            - Conecte ao mongo atlas e crie um banco de dados
            - Defina uma coleção bank para criar os documentos de clientes
            - Insira documentos com a estrutura mencionada
            - Escreve instruções de recuperação de informações com base nos pares
                de chave valor como feito em aula
"""

import pprint
import datetime
import pymongo
import pymongo as pyM

"""Creat access with mongodb database"""
access = pyM.MongoClient(
    "mongodb+srv://roberth:0123456789@cluster0.okaojms.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

"""Variable of access the database clients"""
db = access.client

"""Creating the collections"""
client_collection = db.clients_collection
account_collection = db.accounts_collection

"""Testing if collection is the True in database"""
# print(db.clients_collection)
# print("\n")
# print(db.account_collection)

"""Definindo documento para Clients"""
clients = [
    {
        "name": "roberth",
        "cpf": "01234567891",
        "address": "Rua sao joao, 1900, marinha, maringa - PR"
    },
    {
        "name": "larissa",
        "cpf": "19876543210",
        "address": "Rua joaquina, 933, brasilia, coqual - MA"
    }
]

"""Definindo documento para Accounts"""
accounts = [
    {
        "type": "Current Account",
        "agency": "0001",
        "num": 123456,
        "balance": 2000.00,
        "id_client": 1
    },
    {
        "type": "Savings Account",
        "agency": "0001",
        "num": 654321,
        "balance": 6000.00,
        "id_client": 2
    }
]
"""Insert the collections in database"""
client_collection.insert_many(clients)
account_collection.insert_many(accounts)

print("Clients:")
for client in client_collection.find():
    print("\n")
    pprint.pprint(client)

print("\nAccounts:")
for account in account_collection.find():
    print("\n")
    pprint.pprint(account)

print("\nCount documents")
print(client_collection.count_documents({}))

"""return client the name larissa"""
print(client_collection.count_documents({"name": "larissa"}))

"""return client the num 01234567891"""
print(client_collection.count_documents({"num": "01234567891"}))

"""return client the id 2"""
pprint.pprint(client_collection.find_one({"id": "2"}))

""""Return informations about collection in order"""
print("\nRecuperation collection info in order")
for account in account_collection.find().sort("id"):
    print("\n")
    pprint.pprint(account)

"""Return collections stored in MongoDB client database"""
print("\nStored collections in MongoDB")
collections = db.list_collection_names()
for collection in collections:
    print(collection)
    
"""List collections in database"""
print("\n")
print(db.list_collection_names())

"""Drop database client"""
# client.drop_database('client')