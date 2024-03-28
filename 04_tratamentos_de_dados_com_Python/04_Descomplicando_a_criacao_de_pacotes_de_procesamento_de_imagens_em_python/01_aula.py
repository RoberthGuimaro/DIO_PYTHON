"""
    Objetivos do Projeto

    1 - Entender conceitos relacionados aos pacotes

    2 - Atualizar o projeto e gerar as distribuições

    3 - Publicar o pacote
"""

"""
    Módulo x Pacote

    Módulo - Objeto que serve como unidade organizacional
    do código que é carregado pelo comando de import.

    Pacote - Coleção de módulos com hierarquia.
"""

"""
    Modularização

    Vantagens da modularização:

    - Legibilidade
    - Manutenção
    - Reaproveitamento de código

    Pacote

    Vantagens de criar um pacote:

    - Facilidade de compartilhamento
    - Facilidade de instalação    
"""

"""
    Conceitos

    Pypi - Repositório público oficial de pacotes

    Whell e Sdist - Dois tipos de distribuições

    Setuptools - Pacote usado em setup.py para gerar as distribuições

    Twine - Pacote usado para subir as distribuições no reopsitório Pypi
"""

"""
    Passos

    1 --> Create Project --> Setup.py 
        2 --> Generate Distributions --> Whell / Sdist --> Twine
            3 --> Upload to Pypi --> pip install package_name
"""

"""
    Repositórios disponíveis

    simple-package-template
    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            file1_name.py
            file2_name.py

    package-template
    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            module1_name/
                __init__.py
                file1_name.py
                file2_name.py
            modeule2_name/
                __ini__.py
                file1_name.py
                file2_name.py

    Image-Processing-Package
    image-processing-package/
        README.md
        setup.py
        requirements.txt
        image_processing/
            __init__.py
            processing/
                __init__.py
                combination.py
                transformation.py
            utils/
                __init__.py
                io.py
                plot.py

    https://www.github.com/tiemi
"""

"""
    Passos para criar o projeto
    1 - Fork do template

    2 - Adição do conteúdo dos módulos do projeto

    3 - Edição do arquivo setup.py

    4 - Edição do requirements.txt

    5 - Edição do README.md
"""

"""
    Arquivo setup.py

    Usado para especificar como o pacote deve ser
    construido.
    Documentação:
    https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

"""
    Distribuições

    Para subir o pacote, criar uma distribuição binária ou
    distribuições de código fonte.

    As versões mais recentes do pip instalam primeiramente a
    binária e usam a distribuição de código fonte, apenas se
    necessário. 

    De qualquer forma, iremos criar ambas as distribuições

    whell - Distribuições binárias 
    sdist - Código fonte
"""

"""
    Passos para gerar as distribuições

    1 - Acessar a raiz do projeto

    2 - Comandos de instalação
        python -m pip install --upgrade pip

        python -m pip install --user twine

        python -m pip install --user setuptools

    3 - Comando para criar a distribuição
        python setup.py sdist bdist_whell
"""

"""
    Publicando o pacote no Pypi

    1 - Cria conta no Teste Pypi
        https://test.pypi.org/account/register/

    2 - Publica no Test Pypi
        Comando para publicar no test Pypi:
            python -m twine upload --repository-url
            https://test.pypi.org/legacy/ dist/*

    3 - Instalar o pacote utilizando o Test Pypi
        Comando para instalar o package:
            pip install --index-url https://test.pypi.org/simple/image-processing

    4 - Testar o pacote

    5 - Criar conta no Pypi
        https://pypi.org/account/register/
        
    6 - Publicar no Pypi
        Comando para publicar no Pypi:
            python -m twine upload --repository-url
            https://upload.pypi.org/legacy/ dist/*

    7 - Instalar o pacote usando o Pip
        Comando para instalar o package:
            python -m pip install image_processing
"""

"""
    Documentações adicionais

    Setuptools - https://setuptools.readthedocs.io/en/latest/setuptools.html

    Testes Automatizados - https://docs.pytest.org/en/latest/goodpractices.html

    Uso do Tox - https://tox.readthedocs.io/en/latest/
"""