"""
    Bibliotecas - 
    webbrowser - fornece uma interface de alto nível para permitir a
    exibição de documentos Web aos usuários.

    tkinter - fornece interface padrão do Python para o kit de ferramentas
    gráficas Tk
"""

from tkinter import *
import webbrowser

# Janela do programa
root = Tk( )

# Nome da janela do programa
root.title('Abrir browser')

# Tamanho da janela do programa
root.geometry('300x200')

# Define a função que deverá executar a função de abertura do browser
def google():
    webbrowser.open('www.google.com')

# Cria o botão pertencente ao root, com o nome de abrir google e com o comando google
mygoogle_button = Button(root, text='Abrir o google', command=google)

# Organiza e posiciona o botão na janela do programa.
mygoogle_button.pack(pady=20)

# chama o programa.
root.mainloop()