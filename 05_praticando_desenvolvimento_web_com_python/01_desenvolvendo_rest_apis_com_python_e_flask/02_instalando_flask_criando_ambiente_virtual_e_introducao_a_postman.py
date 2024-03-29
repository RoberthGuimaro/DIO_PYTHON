"""
    PIP

    - Sistema de gerenciamento de pacotes.

    - Utilizado para instalar e gerenciar pacotes/
    bibliotecas em python.

    - Já vem empacotado com Python desde a versão 3.4

    Para instalar o Flask
        pip install Flask
"""

"""
    Virtualenv

    - Ferramenta para criar ambientes Python isolados.

    - Vem integrado com o Python desde a versão 3.3.

    - Estremamente útil para se trabalhar com projetos
    que utilizam bibliotecas com versões diferentes.

    exemplo: python -m venv .\.virtualenvs\minha_virtualenv
    
    ativando a env: .\.virtualenvs\minha_virtualenv\Scripts\activate
"""

"""
    Postaman

    - Ferramenta utilizada para realizar requisições HTTP.

    - Com ela é possível chamar qualquer método e também
    enviar parâmetros.

    - https://www.getpostman.com/downloads/
"""

from flask import Flask

app = Flask(__name__)

@app.route("/<numero>", methods=['GET', 'POST'])
def ola(numero):
    return f"Olá Mundo! {numero}"

if __name__ == "__main__":
    app.run(debug=True)