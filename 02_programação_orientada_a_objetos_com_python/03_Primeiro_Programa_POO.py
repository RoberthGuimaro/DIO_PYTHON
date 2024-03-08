# Nosso primeiro programa POO

# João tem uma bicicletaria e gostaria de registrar
# as vendas de suas bicicletas. Crie um programa
# onde João informe: cor, modelo, ano e valor da 
# bicicleta vendida. Uma bicileta pode: Buzinar,
# parar e correr. Adicione esses comportamentos!


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor  #atributo da classe
        self.modelo = modelo #atributo da classe
        self.ano = ano #atributo da classe
        self.valor = valor #atributo da classe

    #Metodo de classe
    def buzinar(self):
        print("\nBiiiibiiiiiiiii!!!")

    #Metodo de classe
    def parar(self):
        print("\nA bicicleta parou...")

    #Metodo de classe
    def correr(self):
        print("\nA bicicleta está correndo!!!")

    #Metodo de classe
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

cor = input("Informe a cor da bicicleta: ")
modelo = input("Informe o modelo da bicicleta: ")
ano = input("Informe o ano da bicicleta: ")
valor = input("Informe o valor da bicicleta: ")

bike_1 = Bicicleta(cor, modelo, ano, valor)

#Chamando os metodos
bike_1.buzinar()
bike_1.correr()
bike_1.parar()

#Chamando os atributos
print(bike_1.cor, bike_1.modelo, bike_1.ano, bike_1.valor)


#Instanciando outro objeto
bike_02 = Bicicleta("Verde", "Cessi", 1900, 600)

#Chamando o metodo buzinar do segundo objeto
bike_02.buzinar()