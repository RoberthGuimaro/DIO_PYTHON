while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    print(numero)


for numero in range(99):
    if numero == 10:
        continue
    print(numero)