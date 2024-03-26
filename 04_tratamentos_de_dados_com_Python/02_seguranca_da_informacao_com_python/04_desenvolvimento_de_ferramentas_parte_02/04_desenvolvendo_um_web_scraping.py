"""
    Um web scraper é uma ferramenta de coleta de dados da web, uma forma de mineração
    que permite a extração de dados de sites da web convertendo-os em informação
    estruturada para posterior análise.

    Bibliotecas

    from bs4 import BeatifulSoup - É uma biblioteca de extração de dados de arquivos HTML e XML.

    requests - Permite que você envie solicitações HTTP em Python.
"""
# importando as bibliotecas
from bs4 import BeautifulSoup
import requests

# Objeto site, recebe todo o conteúdo da requisicao http do site especificado...
site = requests.get("https://climatempo.com.br/").content

# Objeto soup, recebe o HTML do site, transformando a requisição em HTML
soup = BeautifulSoup(site, 'html.parser')

# prettify, transforma a estrutura HTML em string.
# print(soup.prettify())

# Objeto temperatura, usa o soup para fazer a procura do dado especificado no find.
temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

# Printa o objeto temperatura e o transforma em string.
# print(temperatura.string)

print(soup.title.string)