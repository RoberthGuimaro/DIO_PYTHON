"""
    Biblioteca -
    ctypes - Fornece tipos de dados compatíveis com C e permite funções
    de chamada em DLLs ou bibliotecas compartilhadas.

"""

# Bibliotecas
import ctypes
import os

# Definindo atributo oculto para o arquivo
atributo_ocultar = 0x02

nome_do_arquivo = 'teste.txt'


if not os.path.exists(nome_do_arquivo):
    print("O arquivo não existe")

else:

    # Carregando a bibliotecar kernel32
    kernel32 = ctypes.WinDLL('kernel32')

    # Setando o atributo especifico no arquivo ou pasta especifico
    retorno = kernel32.SetFileAttributesW(nome_do_arquivo, atributo_ocultar)

    if retorno:
        print("Arquivo foi ocultado.")

    else:
        print('Arquivo não ocultado.')