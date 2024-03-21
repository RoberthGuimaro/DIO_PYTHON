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

""" Import framework SQLAlchemy """
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func


Base = declarative_base()

class Client(Base):
    """ Creation client table, insertion informations about client in db """
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    cpf = Column(String(11), nullable=False)
    address = Column(String)

    account = relationship(
        "Account", back_populates="client", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id='{self.id}', name='{self.name}', cpf='{self.cpf}', address='{self.address}')"


class Account(Base):
    """ Creation account table, insertion informations about
    account of client in db """
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    agency = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    client = relationship("Client", back_populates="account")


    """ Método para representar os dados da account"""
    def __repr__(self):
        return f"Account(id='{self.id}', type='{self.type}', agency='{self.agency}', num='{self.num}')"

"""Imprime o nome da tabela Client"""
# print(Client.__tablename__)
"""Imprime o nome da tabela Account"""
# print(Account.__tablename__)

"""Conecction with to db"""
engine = create_engine("sqlite://")

"""Create class like tables in db"""
Base.metadata.create_all(engine)

"""Investigate the db schema, confirming that the table exists"""
inspetor_engine = inspect(engine)
# print(inspetor_engine.has_table("account"))

"""Method searches for the name of db tables"""
# print(inspetor_engine.get_table_names())

"""Return default schema name"""
# print(inspetor_engine.default_schema_name)

"""Create a session with db"""
with Session(engine) as session:
    """Client informations"""
    roberth = Client(
        name= 'roberth',
        cpf= '123456789',
        address= "Rua Quintino, 1141, Jorge, Sao Paulo - SP",
        account = [Account(type='Current Account', agency='0001', num=1)]
    )
    """Client informations"""
    larissa = Client(
        name= 'larissa',
        cpf= '987654321',
        address= "Rua Porfirio, 1010, Quinta, Araras - SP",
        account = [Account(type='Current Account', agency='0001', num=2)]
    )
    """Insert clients informations in db"""
    session.add_all([roberth, larissa])

    """Commit to client informations in db"""
    session.commit()

"""Creates filtering condition to retrieve client"""
stmt = select(Client).where(Client.name.in_(['roberth', 'larissa']))

print("\nUsing filtering condition to retrieve client")
for client in session.scalars(stmt):
    print(client)

"""Variable to retrieve client in an orderly manner"""
stmt_order = select(Client).order_by(Client.id)

print("\nRetrieve client in an orderly manner")
for result in session.scalars(stmt_order):
    print(result)

"""Variable to retrieve total client instances"""
stmt_count = select(func.count('*')).select_from(Client)

print("\nTotal client instances")
for result in session.scalars(stmt_count):
    print(result)