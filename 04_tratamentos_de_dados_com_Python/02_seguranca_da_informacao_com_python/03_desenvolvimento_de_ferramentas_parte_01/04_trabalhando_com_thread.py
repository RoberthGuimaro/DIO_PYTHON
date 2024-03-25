# Importando a classe Thread do modulo threading
from threading import Thread
import time

# Define o objeto carro
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'\nPiloto: {piloto} Km: {trajeto}')

# Implementa o Thread para que os objetos possam competir pelo processo ao mesmo tempo
t_carro_01 = Thread(target=carro, args=[1, 'roberth'])
t_carro_02 = Thread(target=carro, args=[2, 'noan'])

# Chama o objeto e inicia o processo
t_carro_01.start()
t_carro_02.start()