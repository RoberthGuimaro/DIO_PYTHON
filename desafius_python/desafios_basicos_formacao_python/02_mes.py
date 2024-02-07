#''' 
#IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
# - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#   casos, é necessário converter/tratar os dados de entrada; 
# - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#   impressão dos dados de saída. 
#- "dict{}": dicionários possuem uma relação de chave - valor. Para cada chave haverá um valor.
#'''
month = input()

months_dict = {
    '1': "January",
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

print(months_dict[month])
#    ''' 
#    TODO Faça uma relação entre as possíveis entradas e os meses (em inglês).
#    TODO Imprima o valor de cada chave em relação as entradas do programa.
#    '''