# Maiúscula, minúscula e título

curso = "pYtHon"

print(curso.upper()) #Deixa em maiúscula

print(curso.lower()) #Deixa em minúscula

print(curso.title()) #Primeira letra em maiúscula

#Eliminando espaços em branco

curso = "     Python "

print(curso.strip()) #Elimina os espaços dos dois lados da string

print(curso.lstrip()) #Elemina os espaços da esquerda da string

print(curso.rstrip()) #Elimina os espaços da direita da string

#Junções e centralização

curso = "Python" 

print(curso.center(10, "#")) #Centraliza a string primeira ao centro, o primeiro argumento é a quantidade total de caracteres que a string possuira, o segundo argumento é qual caracter sera utilizado para centralizar.
#   exemplo: "##python#"

print(".".join(curso)) #"Junta ou melhor dizendo, usa como separador" o argumento que está dentro das aspas, iterando sobre cada item.
#   exemplo: "p.y.t.h.o.n"