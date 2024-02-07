saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente.")

#----------------------------------------------------------------------------#
    
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente.")

#----------------------------------------------------------------------------#

opcao = int(input("Informe uma opcao: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opcao invalida")

#----------------------------------------------------------------------------#

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("Ainda nao pode tirar a CNH.")

#----------------------------------------------------------------------------#

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda nao pode tirar a CNH.")

#----------------------------------------------------------------------------#

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer aulas praticas.")
else:
    print("Ainda nao pode tirar a CNH.")