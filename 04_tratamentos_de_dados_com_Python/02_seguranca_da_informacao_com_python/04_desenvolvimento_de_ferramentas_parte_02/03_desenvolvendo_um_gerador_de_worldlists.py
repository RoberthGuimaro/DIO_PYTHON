"""
    O que são WORDLISTS?

    Wordlists são arquivos contendo uma palavra por linha. São utilizados
    em ataques de força bruta como quebra de autenticação, pode ser usada
    para testar a autenticação e confidencialidade de um sistema.

    Bibliotecas
    itertools - Está biblioteca fornece condições para iteração como permutação
    e combinação.

    Usaremos essa biblioteca para gerar uma lista com vários caracteres diferentes
    e sem repetição de palavras.
    
"""

import itertools

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))

for caracter in resultado:
    print(''.join(caracter))