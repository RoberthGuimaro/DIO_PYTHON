# O que sao e como utilizamos

## Atributos do Objeto

## Todos os objetos nascem com o mesmo
## numero de atributos de classe e de
## instancia. Atributos de instancia sao
## diferentes para cada objeto (cada objeto
## tem uma copia), ja os atributos de classe
## sao compartilhados entre os objetos.

### Exemplo

class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} - ({self.numero}) - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

    
larissa = Estudante("Larissa", 5467)
roberth = Estudante("Roberth", 2134)
mostrar_valores(larissa, roberth)

larissa.numero = 9874

Estudante.escola = "Python"

gabriel = Estudante("Gabriel", 3698)

mostrar_valores(larissa, roberth, gabriel)