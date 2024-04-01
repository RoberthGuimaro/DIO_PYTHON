from models import Pessoas
from models import db_session

# Insere dados na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(name='Roberth', age=28)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoas
def consulta_pessoas():
    pessoas = db_session.query(Pessoas).all()
    for pessoa in pessoas:
        print(pessoa.name, pessoa.age)

# Realiza alterações na tabela pessoas
def altera_pessoas():
    pessoa = db_session.query(Pessoas).filter_by(name='Roberth').first()
    pessoa.age = 30
    pessoa.save()

# Exlui dados da tabela pessoas
def exclui_pessoas():
    pessoa = db_session.query(Pessoas).filter_by(name='Roberth').first()
    pessoa.delete()

if __name__ == '__main__':
#    insere_pessoas()
#    altera_pessoas()
    consulta_pessoas()
    print('*'*20)
    exclui_pessoas()
    consulta_pessoas()