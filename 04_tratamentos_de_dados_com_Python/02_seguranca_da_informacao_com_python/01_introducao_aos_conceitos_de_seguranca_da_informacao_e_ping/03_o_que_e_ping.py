"""
    1 - O que é ICMP?
            O ICMP (Internet Controle Message Protocol), é um protocolo integrante
            do Protocolo IP utilizado para fornecer relatórios de erros à fonte original.

    2 - O que é PING?
            O ping é uma ferramenta que usa o protocolo ICMP para testar a conectividade
            entre nós. É um comando disponível praticamente em todos os sistemas operacionais
            que consiste no envio de pacotes para o equipamento de destino e na "escuta" das 
            respostas.

            Princípio da disponibilidade.

            ping www.google.com - comum

            ping -n 6 www.google.com - -n 6, quantidade de request enviados
            
    3 - Ferramenta PING simples em Python
            Biblioteca os
                Este módulo fornece uma maneira simples de usar funcionalidades que são
                dependentes de sistema operacional.

    4 - Ferramanta PING múltiplo em Python
"""

""" Ping Simples"""

# import os # importando a biblioteca os

# print("#" * 60)

# ip_ou_host = input("Digite o IP ou host alvo: ")

# print("_" * 60)

# os.system(f'ping -n 6 {ip_ou_host}')


"""Ping Múltiplo"""

import os
import time

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print("Verificando o IP:  ", ip)
        print("-" * 60)
        os.system('ping ' + ip)
        print("-" * 60)
        time.sleep(5)
