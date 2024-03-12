# ORM
# ORM - Object Relational Mapping
# Objeto -> Modelo Relacional
# Mais fácil para o programador
#   CRUD, QUERY, CONEXÂO

## Vantagens
## Menos código
## Melhor manutenção
## Utilização de conectores
## Indicado para CRUDs

###Entidade
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)
    
###ORM
### Desvantagens
### Complixidade X ORM
### Dependência do ORM
### Depende do projeto
### Retorno das consultas sem necessidades de programar na "mão"
    
### Perda de performance
### Deixa de estudar SQL e perde a eficiência na construção
### Número de instâncias x velocidade
    
### ORM
### Por que usar?
### Troca de SGBD mais facilitada
### Modelo MVC
### Deiminuição do DRY
### Evita problemas de segurança
    
#### ORM e SQL
#### Uso de views
#### Melhor dos dois mundos
#### Qual a melhor ferramenta para o seu problema?

    
