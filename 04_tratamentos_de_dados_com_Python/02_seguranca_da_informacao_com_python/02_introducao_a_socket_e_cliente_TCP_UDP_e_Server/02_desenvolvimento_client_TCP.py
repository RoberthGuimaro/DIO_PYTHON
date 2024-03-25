import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print("A conexão falhou!!!")
        print(f"Error: {e}")
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta alvo: ")

    try:
        # Definindo um timeout de 10 segundos para a conexão
        s.settimeout(10)
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f"Cliente TCP conectado com sucesso no host {HostAlvo} na porta {PortaAlvo}")

        s.close() # Aqui fechamos a conexão
        print("Conexão encerrada!")    
    
    except socket.error as e:
        print("A conexão falhou.")
        print(f"Erro: {e}")
        sys.exit()

if __name__ == "__main__":
    main()
