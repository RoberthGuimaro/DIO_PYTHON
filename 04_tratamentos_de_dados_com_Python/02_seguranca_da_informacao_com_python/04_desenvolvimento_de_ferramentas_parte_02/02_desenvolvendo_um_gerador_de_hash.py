import hashlib

# Objeto que recebe o texto a ser utilizado na criação do HASH
string = input('Digite o texto a ser gerado a HASH: ')


menu = int(input(''' ##### MENU - Escolha o tipo de HASH ##### 
             1 - MD5
             2 - SHA1
             3 - SHA256
             4 - SHA512
             
             Digite o número do HASH a ser gerado:
             '''))

if menu == 1:

    # Objeto que recebe o texto convertido em bits, da hashlib md5
    resultado = hashlib.md5(string.encode('utf-8'))

    print(f'O hash MD5 da string, {string} é: {resultado.hexdigest()}')

elif menu == 2:

    # Objeto que recebe o texto convertido em bits, da hashlib md5
    resultado = hashlib.sha1(string.encode('utf-8'))

    print(f'O hash sha1 da string, {string} é: {resultado.hexdigest()}')

elif menu == 3:

    # Objeto que recebe o texto convertido em bits, da hashlib md5
    resultado = hashlib.sha256(string.encode('utf-8'))

    print(f'O hash sha256 da string, {string} é: {resultado.hexdigest()}')

elif menu == 4:

    # Objeto que recebe o texto convertido em bits, da hashlib md5
    resultado = hashlib.sha512(string.encode('utf-8'))

    print(f'O hash sha512 da string, {string} é: {resultado.hexdigest()}')

else:
    print('Valor não identificado.')