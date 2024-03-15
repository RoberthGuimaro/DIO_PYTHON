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


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)


    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"
    

print(User.__tablename__)
print(Address.__tablename__)

#conexao com o banco de dados
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

#investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    roberth = User(
        name= 'roberth',
        fullname= 'Roberth Guimaro',
        address=[Address(email_address='roberth_guimaro@gmail.com')]
    )

    larissa = User(
        name= 'larissa',
        fullname='Larissa Rocha da Silva',
        address = [Address(email_address='Larissa@gmail.com'),
                   Address(email_address='Larissa@hotmail.com')]
    )

    noan = User(
        name= 'noan',
        fullname= 'Noan Gabriel Rocha Guimaro'
    )


    # Enviando para o BD (persistencia de dados)
    session.add_all([roberth, larissa, noan])

    session.commit()

stmt = select(User).where(User.name.in_(['roberth', "larissa"]))

print('\nRecuperando usuarios a partir de condicao de filtragem')

for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))

print("\nRecuperando os enderecos de email de Larissa")

for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname)
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

print("\n")
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

print(select(User.fullname, Address.email_address).join_from(Address, User))


connection = engine.connect()

results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print("\nTotal de instancias de Users")
for result in session.scalars(stmt_count):
    print(result)