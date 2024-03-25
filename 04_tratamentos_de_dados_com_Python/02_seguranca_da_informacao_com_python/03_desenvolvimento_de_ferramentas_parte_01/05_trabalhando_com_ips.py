# Importa a biblioteca ipaddress
import ipaddress

# Objeto que recebe o ip para ser manipulado
ip = '192.168.100.0/28'

# Objeto que irá manipular o ip
rede = ipaddress.ip_network(ip, strict=False)

# Laço que irá imprimir todos os ip's de determinada rede
for ip in rede:
    print(ip)