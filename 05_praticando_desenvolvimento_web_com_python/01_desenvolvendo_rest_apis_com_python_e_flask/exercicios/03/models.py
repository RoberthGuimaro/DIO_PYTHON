"""
    Exercício para praticar

    - Em um novo diretório crie um banco de dados com três tabelas.
    Tabela Programador, tabela Habilidades e uma terceira tabela que
    ligue o programador com a habilidade, cujo nome será
    programador_habilidade

    - A tabela programador deve conter os campos id, nome, idade e email

    - A tabela Habilidades deve conter os campos id e nome

    - A tabela programador_habilidade deve conter os campos id,
    programador (FK com programador) e habilidade (FK com habilidade)
"""

# Importa o método de criação de mecanismo de banco de dados e ferramentas ORM do SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Cria o mecanismo do banco de dados SQLite
folder_path = "/home/roberth/Documents/GitHub/DIO_PYTHON/05_praticando_desenvolvimento_web_com_python/01_desenvolvendo_rest_apis_com_python_e_flask/exercicios/03"
db_path = os.path.join(folder_path, "dev.db")
engine = create_engine('sqlite:///' + db_path)

# Cria a sessão do banco de dados utilizando o mecanismo criado
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# Cria a base de classes declarativas para definição de modelos
Base = declarative_base()
Base.query = db_session.query_property()

class Utils():
    # Método para salvar uma nova instância da classe no banco de dados
    def save(self):
         db_session.add(self)  # Adiciona a instância ao banco de dados
         db_session.commit()  # Confirma as alterações

    # Método para excluir uma instância da classe do banco de dados
    def delete(self):
        db_session.delete(self)  # Remove a instância do banco de dados
        db_session.commit()  # Confirma as alterações


# Define a classe de modelo para a tabela 'programador'
class Programador(Base, Utils):
    __tablename__='programador'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)  # Coluna para armazenar o nome da pessoa
    age = Column(Integer)  # Coluna para armazenar a idade da pessoa
    mail = Column(String) # Coluna para armazenar o e-mail da pessoa

    # Método especial que fornece uma representação string da instância da classe
    def __repr__(self):
        return f'< {self.name} >'

# Define a classe de modelo para a tabela 'habilidades'
class Habilidades(Base, Utils):
    __tablename__='habilidades'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), index=True)  # Coluna para armazenar o nome da habilidade

    def __repr__(self):
        return f'< {self.name} >'
    
class Programador_habilidade(Base):
    __tablename__='programador_habilidade'
    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programador.id'))  # Chave estrangeira para a tabela 'programador'
    programador = relationship("Programador")  # Define o relacionamento com a tabela 'programador'
    habilidades_id = Column(Integer, ForeignKey('habilidades.id'))
    habilidades = relationship("Habilidades")

# Função para inicializar o banco de dados, criando todas as tabelas definidas
def init_db():
    Base.metadata.create_all(bind=engine)

# Chama a função de inicialização do banco de dados se este arquivo for executado diretamente
if __name__ == '__main__':
    init_db()