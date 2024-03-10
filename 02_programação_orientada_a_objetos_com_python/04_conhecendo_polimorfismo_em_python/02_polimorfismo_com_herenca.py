# Mesmo metodo com comportamento diferente

## Na heranca, a classe filha herda os metodos
## da classe pai. No entanto, e possivel modificar
## um metodo em uma classe filha herdada da classe
## pai. Isso e particularmente util nos casos em
## que o metodo herdado da classe pai nao se encaixa
## perfeitamente na classe filha.

### Exemplo

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao voa")

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())