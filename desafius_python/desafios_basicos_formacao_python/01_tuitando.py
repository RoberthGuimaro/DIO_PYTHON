t = input("Digite seu TWEET: ")

quantidade_caracteres = len(t)

if quantidade_caracteres > 140:
    print("MUTE")
else:
    print("TWEET")