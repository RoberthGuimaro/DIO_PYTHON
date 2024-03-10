### Público / Privado

### Todos os recursos são públicos, a menos que
### o nome inicie com underline. Ou seja, o interpretador
### Python não irá garantir a proteção do recurso, mas por
### ser uma convenção amplamanete adotada na comunidade,
### quando encontramos uma variável e/ou método com nome
### iniciado por underline, sabemos que não deveriamos
### manipular o seu valor diretamente, ou invocar o método
### fora do escopo da classe.

#### Exemplo

class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())