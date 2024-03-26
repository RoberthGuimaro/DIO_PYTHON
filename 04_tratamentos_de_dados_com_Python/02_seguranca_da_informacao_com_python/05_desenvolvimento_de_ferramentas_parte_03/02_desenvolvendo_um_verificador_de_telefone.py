""""
    Bibliotecas

    phonenumbers - Fornece vários recursos, como informações básicas de
    um número de telefone, validação de um número de telefone, etc.

"""

#Bibliotecas e módulos
import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone no formato +556740028922:')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

