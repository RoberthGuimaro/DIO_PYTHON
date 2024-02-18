# ''' 
# IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
#  - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#    casos, é necessário converter/tratar os dados de entrada; 
#  - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#    impressão dos dados de saída. 
# '''

# DESAFIO
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal 
# possível segundo o esquema abaixo, da esquerda para a direita.  
# Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o 
# animal segundo a figura acima, com todas as letras minúsculas.

# Saída
# Imprima o nome do animal correspondente à entrada fornecida.

# Entrada               Saida
# vertebrado                 
# mamifero               
# onivoro               homem

# Entrada               Saida
# vertebrado                 
# ave               
# carnivoro             aguia

# Entrada               Saida
# invertebrado                 
# anelideo               
# onivoro               minhoca


a = input()
a = a.lower()

b = input()
b = b.lower()

c= input()
c = c.lower()

if a == 'vertebrado':
    if b == 'ave' and c == 'carnivoro':
        print('aguia')

    elif b == 'ave' and c == 'onivoro':
        print('pomba')

    elif b == 'mamifero' and c == 'onivoro':
        print('homem')

    elif b == 'mamifero' and c =='herbivoro':
        print('vaca')

elif a == 'invertebrado':
    if b == 'inseto' and c == 'hematofago':
        print('pulga')

    elif b == 'inseto' and c == 'herbivoro':
        print('lagarta')

    elif b == 'anelideo' and c == 'hematofago':
        print('sanguessuga')

    elif b == 'anelideo' and c =='onivoro':
        print('minhoca')





# ''' 
# TODO Crie as condições necessárias para definir o tipo de animal possível seguindo
# o esquema da imagem.
# TODO Imprima, de acordo com as condições, o animal identificado.
# '''