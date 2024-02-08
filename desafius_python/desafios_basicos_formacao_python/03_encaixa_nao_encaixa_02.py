#''' 
#IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
# - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#   casos, é necessário converter/tratar os dados de entrada; 
# - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#   impressão dos dados de saída. 
#'''
N = int(input())

while(N >= 0):
    n1 = input()
    n2 = input()

    tamanho_n1 = len(n1)
    tamanho_n2 = len(n2)

    contador = 0
    numerador = N
    indice = -1
    testador = 0

    if (tamanho_n1 > 1000 or tamanho_n2) > 1000:
        print("Voce digitou mais de 1000 caracteres, isso nao e permitido!")
        break
    while(numerador != contador):
        if n1[::indice] == n2[::indice]:
            testador += 1
        contador += 1
        indice -= 1
    if(testador == N):
        print("encaixa")
    else:
         print("nao encaixa")
    
    N -= 1



#    ''' 
#    TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
#    "encaixa" ou "não encaixa" para cada uma das relações N vezes.
#    '''