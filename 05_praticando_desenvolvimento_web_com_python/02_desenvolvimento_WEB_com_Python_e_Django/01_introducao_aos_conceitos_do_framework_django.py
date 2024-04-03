"""
    Objetivos do Curso

    - Aprender mais sobre sistemas WEB

    - Aprender a utilizar Python para desenvolvimento WEB

    - Aprender o framework Django

    - Aprender a manipular informações em banco de dados
    na sua aplicação.
"""

"""
    Sistemas WEB

    - São software/aplicações hospedados na internet/intranet
    onde usuário pode acessar através de requisições http por
    um navegador.

    - Sistemas WEB permitem ser acessados sem a necessidade
    de download e instalação da aplicação.

    - Outra definição de apliacação é... WEB é onde tudo 
    é processado em algum servidor.
"""

"""
    Vantagens de um sistema WEB

    - É seguro, já que a aplicação e o banco são hospedados em
    servidores locais especializados, além de poder contar com
    certificados de segurança.

    - Sistemas WEB são mais acessíveis já que não necessitam de
    realizar download e nem baixar dependência para sua utilização.

    - Mais rápido e menos trabalhoso na disponibilização de novas
    atualizações.
"""

"""
    Python para WEB

    - Python é uma linguagem que é utilizada em muitos seguimentos, como
    Ciência de dados, Administração de sistemas, Desenvolvimento de software
    desktop (GUI), jogos, aplicativos e é claro para Sistemas WEB.

    - Python tem crescido cada vez mais no desenvolvimento de aplicações
    web muito por conta de seus ótimos frameworks, onde o mais usado é o
    Django.

    - Além do Django, existem outros frameworks que auxiliam no desenvolvimento
    web com Python, que também são muito populares, como:
    Flask, Pyramid, Tornado, web2py e Bottle.
"""

"""
    Framework Django

    - Django é um framework web Python de alto nivel que incesntiva o rápido
    desenvolvimento e um design limpo.

    - O Django abstrai muito do trabalho do desenvolvedor, por cuidar de grande
    parte do desenvolvimento web, possibilitando o desenvolvedor focar apenas
    no core da sua aplicação.

    - Django é gratuito e open-source.

    - Django é o framework Python mais popular no mercado.

    - https://www.djangoproject.com/
"""
"""
    Criando um projeto Django

    - Para criar um projeto Django é necessário uma estrutura
    padrão que pode ser criada a partir do comando
    django-admin startproject

    Criando um APP

     - Para criar um app no Django é necessário uma estrutura
     padrão que pode ser criada a partir do comando
     djando-admin startapp meu_app
"""
"""
    MANAGE

    - É um wrapper em volta do django-admin.py

    - Ele delega tarefas para o django-admin.py

    - Responsável por colocar o pacote do projeto no sys.path

    - Ele define a variável de ambiente DJANGO_SETTINGS_MODULE que
    então aponta para o arquivo settings.py

    - Por isso, o manage.py é gerado automaticamente junto ao projeto,
    para facilitar o uso de comandos do django-admin.py (comandos
    administrativos)
"""

"""
    WSGI
    
    - Web Server Gateway Interface - Interface de porta de entrada do
    servidor web.

    - Plataforma padrão para aplicações web em Python.

    - Serve de interface do Servidor Web e a Aplicação Web.

    - O Django com o comando startproject inicia uma configuração WSGI
    padrão para que se possa executar sua aplicação WEB.

    - Quando se inicia a aplicação Django com o comando runserver é
    iniciado um servidor de aplicação web leve. Esse servidor é
    especificado pela configuração WSGI_APPLICATION.
"""
"""
    SETTINGS
    
    - É o responsável pelas configurações do Django.

    - Nele é possível configurar por exemplo apps, conexão com banco de
    dados, templates, time zone, cache, segurança, arquivo estáticos, etc.
"""
"""
    URLS
    
    - É um Schema de URL.

    - Responsável por gerenciar as Rotas das URLs, onde é possível configurar
    pra onde cada rota será executada.

    - É uma forma limpa e elegante para gerenciar URLs.
"""
"""
    VIEWS

    - Responsável por processar e retornar  uma resposta para o cliente que
    fez a requisição.
"""

"""
    MODELS

    - Define o modelo de dados inteiramente em Python.

    - Faz a abstração dos objetos de banco para o Python, transformando todas
    as tabelas em classes e os acessos são feito utilizando linguagem Python,
    onde o Django realiza a transformação para SQL.
"""

"""
    ADMIN
    
    - Interface administrativa gerada automaticamente pelo Django

    - Ele le os metadados que estão nos models e fornece uma interface
    poderosa e pronta para a manipulação de dados.
"""

"""
    STATIC

    - Responsável por armazenar os arquivos estáticos.

    - CSS, JavaScript, imagens...
"""

"""
    TEMPLATES

    - Responsável por armazenar os arquivos HTML.

    - O diretório templates é o diretório padrão para armazenarmos
    todos os conteúdos HTML da nossa aplicação.
"""

"""
    Tabelas padrões do Django

    - O Django já possui tabelas padrões que são utilizadas
    principalmente para parte de segurança e autenticação.

    - É possivel crias as tabelas padrões do Django com o comando
    migrate.

    - Ao criar as tabelas padrões do Django, é necessário criar um
    primeiro usuário para conseguir acessar o painel Django Administration.

    - Para criar um primeiro usuário administrador é necessário utilizar
    o comando createsuperuser.

    - As tabelas padrões consistem em auxiliar e agilizar toda a parte de
    autenticação e também de perfils de acesso.

    - Entre as tabelas padrões estão as tabelas de Usuário, Grupo e de Perfil.

    - Com as tabelas padrões, é possível criar usuários, grupos de usuários e
    definir perfis de qual usuário pode acessar determinado conteúdo.
"""

"""
    Migração de dados no Django

    - Para migrações de dados no Django, é necessário que tenha classe
    criadas.

    - Com as classes criadas, para migração é utilizado o comando migrate.

    - Também pode-se utilizar o comando migrations para criação de um 
    arquivo de migração, sem a necessidade de migrar "as cegas".

    - Também pode-se utilizar o comando sqlmigrate, que ao invés de aplicar
    a migração, é gerado todo o comando para que essa migração possa ser
    efetuada manualmente no banco de dados.
    
"""

"""
    Templates

    - O Django oferece no seu modelo de templates a capacidade de se
    utilizar expressões Python no HTML.

    - Com isso é possível mostrar informações e realizar comandos como
    IF e FOR.

    
"""
