texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() # Adiciona quebra de linha



# exemplo utilizando a funcao built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")