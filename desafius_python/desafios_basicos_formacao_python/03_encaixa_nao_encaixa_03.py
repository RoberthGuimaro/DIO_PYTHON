# Função para verificar se B corresponde aos últimos dígitos de A
def encaixa(A, B):
    # Verifica se o comprimento de B é maior que o comprimento de A
    if len(B) > len(A):
        return False
    # Compara os últimos dígitos de A com B
    if A[-len(B):] == B:
        return True
    else:
        return False

# Número de casos de teste
N = int(input("Digite o número de casos de teste: "))

# Loop sobre os casos de teste
for _ in range(N):
    # Entrada dos valores A e B
    A, B = input("Digite os valores de A e B separados por espaço: ").split()
    # Verifica se B encaixa em A e imprime o resultado
    if encaixa(A, B):
        print("encaixa")
    else:
        print("nao encaixa") 