# Mas o que é Flask?
# Flask é um pequeno framework web escrito em python. É classificado
# como um microframework porque não requer ferramentas ou bibliotecas
# particulares, mantendo um núcleo simples, porém, extensível.

# O Flask Python é basicamente um framework do tipo "Faça você mesmo".
# Isso significa que não tem nenhuma interação interna com banco de dados,
# mas o pacote flask-sqlalchemy irá conectar o banco de dados SQL a um
# aplicativo Flask. O pacote flask-sqlalchemy precisa somente de uma coisa
# para se conectar ao banco de dados SQL: o banco de dados URL.

## O Flask precisa que o banco de dados URl seja parte da sua configuração
## central através do atributo SQLALCHEMY_DATABASE_URL. Uma solução rápida
## para isso é fazer um hardcode do banco de dados dentro do aplicativo.

# top of app.py
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URL'] = 'postgres://localhost:5432/flask_todo'
#db = SQLAlchemy(app)

### Simplicidade
### Você pode tornar as coisas mais simples utilizando variaveis de ambiente.
### Elas irão garantir que independentemente da máquina que você rode o código,
### ele irá sempre apontar na coisa certa, se essa coisa estiver configurada no
### ambiente que está sendo rodado. Ele também garante que, mesmo que você precise
### da informação para rodar o aplicativo, nunca irá aparecer como um valor Hardcode
### no source control.

### No mesmo lugar que vocẽ declarou o FLASK_APP, declare um DATABSE_URL apontando
### para o lugar do seu banco de dados Postgres. O desenvolvimento tende a funcionar
### localmente, então aponte para o seu banco de dados local.

# Também no seu script active
#export DATABASE_URL='postgres://localhost:5432/flask_todo'

### Agora em app.py inclua o banco de dados URL no seu aplicativo WEB.

#app.config['SQLALCHEMY_DATABASE_URL'] = os.environ.get('DATABASE_URL',")
#db = SQLAlchemy(app)

### E simplesmente dessa forma, o seu aplicativo agora tem uma conexão 
### com um banco de dados.