# Importando biblioteca hashlib
import hashlib

# Arquivos para comparação de hash
arquivo_01 = 'a.txt'

arquivo_02 = 'b.txt'

# Variavel com o tipo de algoritmo utilizado para o hash
hash_01 = hashlib.new('md5')

# Passa o arquivo que será feito a comparação de has, abre ele em modo leitura binaria
# e lê o arquivo para poder fazer a comparação do hash.
hash_01.update(open(arquivo_01, 'rb').read())

# Variavel com o tipo de algoritmo utilizado para o hash
hash_02 = hashlib.new('md5')

# Passa o arquivo que será feito a comparação de has, abre ele em modo leitura binaria
# e lê o arquivo para poder fazer a comparação do hash.
hash_02.update(open(arquivo_02, 'rb').read())

# Se o resultado passado para o update do hash_01, resumido pelo digest(), for diferente
# do resultado passado para o update do hash_02, então imprimirá  
if hash_01.digest() != hash_02.digest():
    print(f'O arquivo: {arquivo_01} é diferente do arquivo: {arquivo_02}')
    print(f'O hash do arquivo a.txt é: {hash_01.hexdigest}')
    print(f'O hash do arquivo b.txt é: {hash_02.hexdigest}')

else:
    print(f'O arquivo: {arquivo_01} é igual ao arquivo: {arquivo_02}')
    print(f'O hash dos dois arquivos é: {hash_01.hexdigest}')
