"""
    Bibliotecas a serem utilizadas:

        random - Implementa geradores de números, letras e simbolos aleatórios
            para várias situações.

        string - Implementa oprações comuns para strings.
"""

# Importando bibliotecas e métodos necessários
import random
import string

# Variável de entrada de tamanho da senha
tamanho = int(input('Digite o tamanho da senha desejada: '))

# Variável utilizada para definir quais tipos de caracteres serão utilizados na senha
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'

# Variável utilizada para fazer a aleatoriedade
rnd = random.SystemRandom()

# Lógica para criação da senha e print dos caracteres formados
print(''.join(rnd.choice(chars) for i in range(tamanho)))