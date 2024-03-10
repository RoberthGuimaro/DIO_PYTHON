# O que sao e quando utilizamos

## Metodos de Classe

## Metodos de classe estao ligados a clases
## e nao ao objeto. Eles tem acesso ao estado
## da classe, pois recebem um parametro que
## aponta para a classe e nao para a instancia
## do objeto.

### Metodos estaticos

## Um metodo estatico nao recebe um primeiro
## argumento explicito. Ele tambem e um metodo
## vinculado a classe e nao ao objeto da classe.
## Este metodo nao pode acessar ou modificar
## o estado da classe. Ele esta presente em uma
## classe porque faz sentido que o metodo esteja
## presente na classe.

#### Metodos de classe X metodos estaticos

# Um metodo de classe recebe um primeiro parametro
# que aponta para a classe, enquanto um metodo
# estatico nao.

# Um metodo de classe pode acessar ou modificar
# o estado da classe enquanto um metodo estatico
# nao pode acessa-lo ou modifica-lo.

##### Quanto utilizamos o metodo de classe ou estatico

# Geralmente usamos o metodo de classe para criar
# metodo de fabrica.

# Geralmente usamos metodos estaticos para criar
# funcoes utilizarias.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nasciemento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nasciemento(1996, 5, 10, "Roberth")

print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))