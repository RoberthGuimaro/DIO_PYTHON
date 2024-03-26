"""
    Web Crawler - 

    É uma ferramenta usada para encontar, ler e indexar páginas de um site.
    É como um robô que captura informações de cada um dos links que encontra
    pela frente, cadastra e compreende o que é mais relevante. (Palavras - Chaves).

    Muito utilizado em levantamento de informações em um processo de Pentest.

    Bibliotecas
    
    BeautifulSoup - biblioteca de extração de dados de arquivos HTML e XML.

    operator - exporta um conjunto de funções eficientes correspondentes aos
    operadores intrínsecos do Python como: + - * / not and.

    collections - nos ajuda a preencher e manipular eficientemente as estruturas
    de dados como tuplas, dicionários e listas.
"""

# Bibliotecas
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):

    # Lista vazia para armazenar o conteúdo do site
    wordlist = []
    
    # Objeto que cria a requisição da url especifica e transforma em texto
    source_code = requests.get(url).text

    # Objeto que faz a requisição dos dados da URL 
    soup = BeautifulSoup(source_code, 'html.parser')

    # Laço que procura dentro do conteudo do soup, tudo que for div e class
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        
        # Objeto que ira armazenar o conteúdo encontrado
        content = each_text.text

        # Objeto que ira transformar o conteúdo em minusculo e separar o conteúdo por linha
        words = content.lower().split()

        
        for each_word in words:
            wordlist.append(each_word)
        
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    
    clean_list = []

    for word in wordlist:
        symbols = '!@#$%*()_-+=[{]}|\;:"<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")