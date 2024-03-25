import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso!")

host = 'localhost'
port = 5433
message = '\nOla servidor.'

try:
    print(f"Cliente: {message}")

    s.sendto(message.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")

finally:
    print('\nCliente: Fechando a conexao')
    s.close()