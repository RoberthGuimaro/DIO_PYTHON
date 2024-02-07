t = input("Digite seu TWEET: ")

quantidade_caracteres = len(t)

teste = "TWEET" if quantidade_caracteres < 140 else "MUTE"

print(teste)