from models import *
from models import db_session

# Insere dados na tabela pessoas
def insere_programador():
    programador = Programador(name='Larissa', age=26, mail='larissa@gmail.com')
    print(programador)
    programador.save()

# Realiza consulta na tabela pessoas
def consulta_programador():
    programador = db_session.query(Programador).all()
    for dev in programador:
        print(dev.name, dev.age, dev.mail)

# Realiza alterações na tabela pessoas
def altera_programador():
    programador = db_session.query(Programador).filter_by(name='Roberth').first()
    programador.age = 30
    programador.mail = 'guimaro@guimaro.com'
    programador.save()

# Exlui dados da tabela pessoas
def exclui_programador():
    programador = db_session.query(Programador).filter_by(name='Larissa').first()
    print(f'Programador excluido: {programador.name}')
    programador.delete()

def insere_habilidade():
    habilidade = Habilidades(name='HTML')
    print(habilidade)
    habilidade.save()

def consulta_habilidade():
    habilidades = db_session.query(Habilidades).all()
    for habilidade in habilidades:
        print(habilidade.name)

def altera_habilidade():
    habilidade = db_session.query(Habilidades).filter_by(name='HTML').first()
    habilidade.name = 'Python'
    habilidade.save()

def exclui_habilidade():
    habilidade = db_session.query(Habilidades).filter_by(name='HTML').first()
    print(f'Habilidade excluida: {habilidade.name}')
    habilidade.delete()

if __name__ == '__main__':
#    insere_programador()
#    print('*'*10)
#    consulta_programador()
#    print('*'*10)
#    altera_programador()
#    exclui_programador()
#    print('*'*10)
#    consulta_programador()
#    print('*'*10)
#    insere_habilidade()
#    altera_habilidade()
    exclui_habilidade()
    print('*'*10)
    consulta_habilidade()