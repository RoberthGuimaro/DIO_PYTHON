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

"""
    Import framework SQLAlchemy
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()

"""
    Creation client table, insertion informations about client in db
"""
class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    cpf = Column(String(9), nullable=False)
    address = Column(String)

    account = relationship(
        "Account", back_populates="account", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User ( id = {self.id}, name = {self.name}, cpf = {self.cpf}, address = {self.address})"

"""
    Creation account table, insertion informations about
    account of client in db
"""
class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    agency = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    client = relationship("Client", back_populates="account")

    def __repr__(self):
        return f"Account ( id = {self.id},
        type = {self.type}, agency = {self.agency},
        num = {self.num})"
    