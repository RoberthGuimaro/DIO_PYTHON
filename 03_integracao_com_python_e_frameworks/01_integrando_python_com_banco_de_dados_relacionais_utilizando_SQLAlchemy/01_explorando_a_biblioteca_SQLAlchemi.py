# SQLAlchemy

# Framework - Open Source
# Licença MIT - 2019
# Mapeamento Objeto Relacional

## Suporte à:
## Database                 Fully Tested in CI              Normal Support      Best Effort
## Microsoft SQL Server     2017                            2012+               2005+
## MySQL / MariaDB          5.6, 5.7, 8.0 / 10.4, 10.5      5.6+ / 10+          5.0.2+ / 5.0.2+
## Oracle                   11.2, 18c                       11+                 8+
## PostgreSQL               9.6, 10, 11, 12, 13, 14         9.6+                8+
## SQLite                   3.21 3.28+                      3.12+               3.7.16+


### Dialetos Externos

### Database                                            Dialect
### Actian Avalanche, Vector, Actian X and Ingress      sqlalchemy-ingress
### Amazon Redshift (via psycopg2)                      sqlalchemy-redshift
### Apache Drill                                        sqlalchemy-drill
### Apache Druid                                        pydruid
### Apache Hive and Presto                              PyHive
### Apache Solr                                         sqlalchemy-solr
### CockroachDB                                         sqlalchemy-cockroachdb
### CrateDB [1]                                         crate-python
### EXASolution                                         sqlalchemy_exasol
### Elasticsearch (readonly)                            elasticsearch-dbapi

#### Vastamente utilizado
#### Framework completo
#### Flexibilização do SQL
#### Segurança nas instruções

##### Recursos
##### ORM e CORE
##### Suporte a dialetos
##### Manipulação do BD por meio de Transações
##### Suporte a Queries complexas via ORM
##### Config: relações e relacionamentos
##### Sessões, eventos...


###### Extensões
###### I/O assíncrono
###### Associação com proxy
###### Indexação
###### APIs especiais
###### ...

# Exemplo:
from sqlalchemy import Column, JSON, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.indexable import index_property

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    data = Column(JSON)

    name = index_property('data', 'name')

