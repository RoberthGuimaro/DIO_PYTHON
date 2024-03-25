import socket

# obejto de conexao
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso.')

# objeto host
host = 'localhost'
# objeto port
port = 5432

# Ligacao entre cliente/servidor
s.bind((host, port))
mensagem = '\nServidor: Ola cliente.'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("\nservidor enviando mensagem....")

        s.sendto(dados + (mensagem.encode()), end)