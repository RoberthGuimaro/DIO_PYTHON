"""
    SQLAlchemy

    - É um ORM para Python.

    - Um ORM (Object-Relational Mapping) em português Mapeamento
    Objeto-Relacional, ajuda na abstração das tabelas de banco
    de dados na orientação à objeto.

    - Em ORMs tabelas viram classes e o desenvolvedor não precisa
    ter conhecimento em SQL.

    - SQLAlchemy fornece um conjunto completo de padrões de persistência,
    projetasdos para acesso a banco de dados efieicnete e de alto desempenho,
    adaptado em uma linguagem de domínio Pythonica simples.
"""
"""
    SQLite

    - É uma biblioteca de linguagem C que implementa um mecanismo de banco
    de dados pequeno, rápido e autônomo.

    - É o mecanismo de bando de dados mais usado no mundo.

    - Ele é incorporado em smarthpones por exemplo.

    - Com o SQLite é possível montar uma instância de banco de dados sem
    precisar realizar uma instalação de um banco.

    - É muito prático para ambientes de desenvolvimento.
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
folder_path = "/home/roberth/Documents/GitHub/DIO_PYTHON/05_praticando_desenvolvimento_web_com_python/01_desenvolvendo_rest_apis_com_python_e_flask/07_Rest_API_com_presistencia_em_banco_de_dados"
db_path = os.path.join(folder_path, "atividades.db")
engine = create_engine('sqlite:///' + db_path)

# Cria a sessão do banco de dados utilizando o mecanismo criado
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# Cria a base de classes declarativas para definição de modelos
Base = declarative_base()
Base.query = db_session.query_property()

# Define a classe de modelo para a tabela 'pessoas'
class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)  # Coluna para armazenar o nome da pessoa
    age = Column(Integer)  # Coluna para armazenar a idade da pessoa

    # Método especial que fornece uma representação string da instância da classe
    def __repr__(self):
        return f'<Pessoa {self.name}>'

    # Método para salvar uma nova instância da classe no banco de dados
    def save(self):
         db_session.add(self)  # Adiciona a instância ao banco de dados
         db_session.commit()  # Confirma as alterações

    # Método para excluir uma instância da classe do banco de dados
    def delete(self):
        db_session.delete(self)  # Remove a instância do banco de dados
        db_session.commit()  # Confirma as alterações

# Define a classe de modelo para a tabela 'atividades'
class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))  # Coluna para armazenar o nome da atividade
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))  # Chave estrangeira para a tabela 'pessoas'
    pessoa = relationship("Pessoas")  # Define o relacionamento com a tabela 'pessoas'

# Função para inicializar o banco de dados, criando todas as tabelas definidas
def init_db():
    Base.metadata.create_all(bind=engine)

# Chama a função de inicialização do banco de dados se este arquivo for executado diretamente
if __name__ == '__main__':
    init_db()