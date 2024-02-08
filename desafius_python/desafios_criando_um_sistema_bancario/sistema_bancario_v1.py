menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>   """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Você depositou R$ {deposito:.2f}\n"
            print(f"Você depositou R$ {deposito:.2f} em sua conta.\n")
        else:
            print("Valor digitado é inválido.")
    
    elif opcao == "s":
        print("Sacar")
        saque = float(input("Digite o valor  que deseja sacar: "))
        
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingidos no dia.")
        elif saque > limite:
            print("Saque maior que o limite permitido, seu limite é de R$500,00")
        elif saque > saldo:
            print("Valor de saque maior que o saldo em conta.")
        else:
            saldo -= saque
            extrato += f"saque de R${saque:.2f}\n"
            numero_saques += 1
            print(f"Você sacou R${saque:.2f} da sua conta.\n")

    elif opcao == "e":
        print("\n========== Extrato ==========")
        print("Sem movimentações." if not extrato else extrato)
        print("============================")

    elif opcao == "q":
        print("Obrigado por ser nosso cliente. Encerrando aplicação.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")