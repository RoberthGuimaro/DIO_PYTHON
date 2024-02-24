def menu ():
    escolha = input('''
    =====   Escolha a opção que deseja  =====

            [d] Depositar
            [s] Sacar
            [e] Extrato
            [u] Criar Usuário
            [c] Criar Conta
            [l] Listas Contas
            
            [q] Sair
          
    =====   Obrigado por utilizar nossos serviços   =====
    ''')

    return escolha

def depositar(saldo, extrato, /):
    print("Depósito")
    deposito = float(input("Digite o valor que deseja depositar: "))

    if deposito > 0:
        saldo += deposito
        extrato += f"Você depositou R$ {deposito:.2f}\n"
        print(f"Você depositou R$ {deposito:.2f} em sua conta.\n")
    else:
        print("Valor digitado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):

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
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== Extrato ==========")
    print(f"Sem movimentações. Saldo atual: {saldo:.2f}" if not extrato else extrato)
    print("============================")

    return extrato

def criar_usuario(usuarios):
    cpf = input("Informe apenas os números do seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
          print("Este CPF já está cadastrado no sistema!")

    nome = input("Informe seu nome completo, por favor: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço, logradouro, nº - bairro - cidade / UF: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!!!")
     

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário que será cadastrado: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("Conta criada com sucesso!!")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrado, encerrando operação.")

def listar_contas(contas):
     for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("==================")
        print(linha)


def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    while True:
        escolha = menu()

        if escolha == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif escolha == "s":
            saldo, extrato, numero_saques = sacar(saldo = saldo, extrato = extrato, limite = limite, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)

        elif escolha == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif  escolha == "u":
            criar_usuario(usuarios)
        
        elif escolha == "c":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)

        elif escolha == "l":
             listar_contas(contas)

        elif escolha == "q":
            print("Obrigado por ser nosso cliente. Encerrando aplicação.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()