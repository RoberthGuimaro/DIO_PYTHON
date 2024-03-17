# Definindo Objetos em Flask
# Ter um banco de dados para estar conectado é um ótimo primeiro passo.
# Agora é hora de definir alguns objetos para preencher o banco de dados...

# No desenvolvimento de aplicativos, um "model" refere-se a representação
# real ou conceitual. Por exemplo, caso esteja fazendo um app para uma
# concessionária de carros, você talvez defina um model chamdo CAR que
# encapsule todos os atributos e comportamento do carro.

# Nesse caso, você estará falando de um To-do List com Tasks, e cada Task
# pertence a um usuário. Antes de você pensar mais a fundo sobre como eles
# estão relacionados, comece definindo os objetos para Tasks e Users.

# O pacote flask-sqlalchemy aproveita o SQLalchemy para configurar e informar
# a estrutura do banco de dados. Você irá definir um modelo que irá viver no
# no banco de dados herdando do objeto db.Model e irá definir o atributo desses
# models como instâncias db.Column. Para cada coluna, você deve especificar um
# tipo de dado, e então você irá passar esse data type para o comando db.Column
# como primeiro argumento...
# fonte: https://harve.com.r/blog/programacao-python-blog/introducao-e-tutorial-ao-flask-python/

# Pelo fato da definição do model ocupar um espaço conceitural diferente do que da
# configuração do aplicativo, faça com que o models.py mantenha definições de mode
# de forma separada do app.py. O modelo do Task deve ser construído para que tenha
# os seguintes atributos:

# id: Um valor que é um identificador único para puxar do banco de dados.
# name: O nome ou o título da task que o usuário irá ver quando task for listada.
# note: Quaisquer comentários adicionais que uma pessoa queira deixar com sua task.
# creation_date: A data e o horário que a task foi criada.
# due_date: A data e o horário que a task deve ser concluída (se houver).
# completed: Uma forma de indicar se a task foi concluída ou não.
# fonte: https://harve.com.r/blog/programacao-python-blog/introducao-e-tutorial-ao-flask-python/

# Dado essa lista de atributos para objetos Task, o objeto Task do aplicativo pode
# ser deffinida dessa forma:

# from .app import db
# from datetime import datetime

# class Task(db.Model)
# """Task for the To Do list."""
# id = db.Column(db.Integer, primary_key=True)
# name = db.Column(db.Unicode, nullable=False)
# note = db.Column(db.Unicode)
# creation_date = db.Column(db.DateTime, nullable=False)
# due_date = db.Column(db.DateTime)
# completed = db.Column(db.Boolean, default=False)

# def __init__(self, *args, **kwargs):
# """On construction, set date of creation."""
# super().__init__(*args, **kwargs)
# self.creation_date = datetime.now()

## Relacionamento dos models
## Em certos aplicatios web, você talvez queira expressas relacionamentos
## entre objetos. No exemplo do To-do List, usuários são donos de várias task,
## e cada tarefa pertence  a somente a um usuário.

## Esse é um exemplo de um relacionamento "many-to-one", também conhecido como
## foreign key relationship, onde as tasks são os "many" (muitos) e o usuário
## dono delas é o "one" (um).

## No Flask Python, um relacionemtno many-to-one pode ser especificado utilizando
## a função db.relationship. Primeiro, construa o objeto User.

## class User(db.Model):
## """The User object that owns tasks."""
## id = db.Column(db.Integer, primary_key=True)
## username = db.Column(db.Unicode, nullable=False)
## email = db.Column(db.Unicode, nullable=False)
## password = db.Column(db.Unicode, nullable=False)
## date_joined = db.Column(db.DateTime, nullable=False)
## token = db.Column(db.Unicode, nullable=False)

## def __init__(self, *args, **kwargs):
## """On construction, set date of creation."""
## super().__init__(*args, **kwargs)
## self.date_joined = datetime.now()
## self.token = secrets.token_urlsafe(64)

### Inicializando o banco de dados
### Agora que os modelos e os relacionamentos de modelos estão configurados,
### comece configurando o sue banco de dados. O Flak Python não vemcom a sua
### própria utilidade de gerenciamento de banco de dados, então você terá que
### escrever o seu pŕoprio (até um certo ponto).

### Crie um scrit chamado initializedb.py pŕoximo do setup.py para gerenciar
### o banco de dados. (Claro, não precisa ser chamado assim, mas porque não dar
### nomes que são apropriados a função do arquivo?) Dentro de initializedb.py,
### importe o objeto db de app.py e use-o para criar e eliminar tabelas.
### initializedb.py deve parecer dessa forma:

### from todo app import db
### import os
###
### if bool(os.environ.get('DEBUG',")):
###     db.drop_all()
### deb.create_all()

#### Views e Configurações da URL
#### As últimas partes necessárias para conectar o aplicativo inteinro são os
#### views e routes. Em desenvolvimento web, um "view" (conceito) é uma funcionalidade
#### que roda quando um ponto de acesso específico ("route") é atingido.

#### Em Flask, views aparecem como funções, por exemplo, consegue ver a view "hello world".
#### Quando o route do http://ddomainname/ é acessado, o cliente recebe a resposta, "Hello World!".

#### @app.route('/')
#### def helo_world():
#### """Print 'Hello, world!' as the response body."""
####    return 'Hello, world!'

#### Comece por uma view que lida somente com solicitações get, e reponda com o JSON
#### representando todos os routes que serão acessíveis e os métodos que podem ser
#### utilizados para acessar elas:

#### from flask import jsonify

#### @app.route('/api/v1', methods=["GET"])
#### def info_view():
####    """List of routes for this API."""
####    output = {
####        'info': 'Get/api/v1',
####        'register': 'POST/api/v1/accounts',
####        'single profile detail': 'GET/api/v1/accounts/<username>',
####        'edite profile': 'PUT/api/v1/accounts/<username>',
####        'delete profile': 'DELETE/api/v1/accounts/<username>,
####        'login': 'POST/api/v1/accounts/login',
####        'logout': GET/api/v1/accounts/logout',
####        "user's tasks": 'GET/api/v1/accounts/<username>/tasks',
####        "creat task": 'POST/api/v1/accounts/<username>/tasks',
####        "task detail": 'GET/api/v1/accounts/<username>/tasks/<id>',
####        "task update": 'PUT/api/v1/accounts/<username>/tasks/<id>',
####        "delete task": 'DELETE/api/v1/accounts/<username>/tasks/<id>'
####    }
####    return jsonify(output)

#### A função view encima pega o que é efetivamente uma lista de to-do o
#### route que esse API pretende ligar e envia ao cliente toda vez que o
#### route http://domainname/api/v1 for acessada. Tenha em mente que, por
#### si mesmo, o Flask oferece suporte ao roteamento para URLs exatamente
#### iguais, então acessar essa rota com um trailing / iria criar um erro
#### 404. Se você quisesse lidar com a mesma função view, você precisaria
#### de um stack de decoradores dessa forma:

#### @app.route('/api/v1', methods= ["GET"])
#### @app.route('/api/v1/', methods= ["GET"])
#### def info_view():
####    conteudo do método.