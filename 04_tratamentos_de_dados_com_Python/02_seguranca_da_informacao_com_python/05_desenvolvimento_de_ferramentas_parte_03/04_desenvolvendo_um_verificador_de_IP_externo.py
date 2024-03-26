"""
    Bibliotecas - 
    re - Permite operações com expressões regulares

    json - Fornece operações de codificação e decodificação em JSON

    from urlib.request import urlopen - Funções e classes que ajudar a abrir URLs

    http://ipinfo.io/json
"""

import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

reposta = urlopen(url)

dados = json.load(reposta)

ip = dados['ip']

org = dados['org']

city = dados['city']

pais = dados['country']

region = dados ['region']

print('Detalhes do IP externo\n')
print(f'IP: {ip}\n Org: {org}\n City: {city}\n Country: {pais}\n Region: {region}')