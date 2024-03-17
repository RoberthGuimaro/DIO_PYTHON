# MTV - Model Template View
# Variação do MVC (Model View Controller)

# MTV - Model Template View
# Todo o desenvolvedor deve ao menos saber qual o objetivo
# deste padrão de desenvolvimento. Separa-se as regras de
# negócios (controlador), os dados e métodos de acessos aos
# mesmos (modelo) e as regras de apresentação (visualização).
# Desse modo, caso ocorra alguma alteração na sua camada de
# visualização (digamos que sua aplicação ganhe uma versão mobile).

# No caso do Django, há uma variação deste modelo que é o MTV (Model
# Template View). Aqui entramos em um assunto que gera bastante
# discussão entre os iniciantes
# Django: aonde raios está o Controller?

# O Framework é o Controlador
# Em Django, o controlador não é responsável pela lógica do neǵocio
# e sim pelo funcionamento do seu projeto. Além de models, views e
# templates, em Django nós temos também url dispatchers, middlewares
# e handlers. E é este "além" que o Django encara como Controller.

# Somos capazes de incrementar o controlador do Django, por exemplos,
# somos obrigados a criar regras de urls dizendo ao Django que ao receber
# uma requisição para a URL X, ele deverá acionar a view Y.

# Models
# Em Models, escrevemos classes que desinarão nossas tabelas no banco de dados
# e manipularemos estas atráves de orientação a objetos (ORM - Mapeamento
# Objeto Relacional), Você não precisa escrever absolutamente nada de SQL,
# há não ser que seja estritamente necessário.

# Você também não precisa se preocupar muito com que o banco vai usar - já
# que o ORM do Django suporta MySQL, PostgreSQL, SQLite e até mesmo Oracle.

# Views
# Em Views escrevemos as regras de apresentação. Calma lá... não chegamos nos
# templates ainda. Estamos falando de criar funções que têm por parâmetro um
# objeto de requisição (request) e por retorno um objeto de resposta (response).
# O "meio de campo" entre estes extermos é justamente a responsabilidade a sua View....

# O que muita ente entende por "regras de negócios de sistema" será escrito na View.
# É nela que dizemos qual modelo deve ser instanciado, o que ee deve fazer, qual template
# deve ser importado, como o valor deve ser exibido nele e qual resposta deve ser enviada
# para o internauta (um HTML, um XML, um SVG, um redirecionamento, um erro 404, um erro 500, etc.).

# Em Django, escrevemos formulários em classes geralmente situadas no arquivo forms.py
# Logo, podemos escrever as regras de comportamento de um formluário dentro de sua classe,
# tirando esta responsabilidade da View. Isto é interessante pois, se usarmos um formulário
# em mais de uma View não é necessário duplicar código (DRY).

# Templates
# Não engane-se...template não refere-se apenas a HTML!

# Podemos escrever templates para HTML, JavaScript, CSS, XML, YAML, JSON, SVG,
# qualquer coisa. Na View você indica qual será o tipo  de resposta, o template
# é só a forma de apresentar o que a View "preparou".

# O sistema de templates do Django é uma de suas mais notórias funcionalidades.
# Com ele podemos criar herenças, ou seja, um template base contendo a estrutura básica
# do seu webtsite e templates específicos que herdam as características deste template
# base e atribuem/criam suas pŕoprias características. Acredite, controlar as meta-tags
# do seu website nunca foi tão fácil... e nem é necessário uma aplicações para isso,
# basta saber um pouco de HTML.

# Dentro desta estrutura de desenvolvimento, é muito fácil separar as funções do
# WebProgrammer e do WebDesigner. O sistema de templates do Django possui sintaxe
# própria e simples. O programador só preocupa-se com os dados que ele deve enviar
# para o template, o designer só preocupa-se com que dados ele irá receber.


# Modelagem de Sistemas
# Dentro desta estrutura de desenvolvimento, é muito fácil seprar as funções do
# WebProgrammer e do WebDesigner.

## Projetos, Aplicações e "Plugabilidade"
## Em Django, iniciamos um projeto com a simpática sintaxe em um terminal do seu SO:
##      python manage.py startapp <nome-da-sua-aplicacao>

## Ele criará uma pasta com o nome do seu projeto que conterá os arquivos:
##      __init__.py: É o arquivo que determina que aquela pasta é um pacote Python.
##      settings.py: Arquivo de configurações em XML? Esqueça! Em Django temos a
##      configuração do nosso projeto em um único arquivo .py.
##      urls.py: Este é o "temido" url dispatcher. Você passará bons e maus momentos com ele.
##      manage.py: O regente da orquestra. É através dele que você executará ações como criar
##      uma aplicação, sincronizar o banco de dados, iniciar o servidor web embutido (somente
##      recomendado para ambiente de desenvolvimento), etc. Esse é um dos caras que fará o seu
##      dia bem melhor com o Django.

## Novamente, você não precisa executar o manage.py startapp para iniciar uma aplicação, é
## apenas praticidade

## Para o Django, um Projeto é um conjunto de aplicações. Na prática: digamos que você irá
## desenvolver um website para o cliente Bikes do Roberth. Então poderia chamar o seu projeto
## de biker_do_roberth e a partir daí desenvolver as aplicações necessárias pra o funcionamento
## do website.

## Além do seu "CORE", o Django disponibiliza uma série de recursos que os Pythonistas costumam
## chamar de "Baterias Inclusas".

## Dentre os recursos mais comuns, temos à disposição o auth, sites, admin, contenttypes, etc.
## Sem eles, o seu website funciona. Com eles, você economiza quilometros de LOC e terá aplicações
## testadas à exaustão.
## https://www.profissionaisti.com.br/entendendo-o-django

## CRUD
## Este exemplo gira em torno da implementação completa de Visualições Baseadas em Classes no Django
## (Criar, Recuperar, Atualizar, Excluir). Vamos discutir o que realmente significa o CRUD...

##                              CRUD
##      _________________________|_____________________________
##      |           |                       |                 |
##    Create      Retrieve                Update            Delete


## Create View - Cria ou adiciona novas entradas em uma tabela no banco de dados.

## Recuperar Visualizações - Ler, recuperar, pesquisar ou visualizar entradas existentes como uma
## lista (ListView) ou recuperar uma entrada específica em detalhes (DetailView).

## UpdateView - Atualizar ou editar entradas existentes em uma tabela no banco de dados.

## DeleteView - Excluir, desativar ou remover entradas existentes em uma tabela no banco de dados.

## FormView - Renderizar um formulário para modelo e manipular os dados inseridos pelo usuário.

