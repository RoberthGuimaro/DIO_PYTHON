from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')

def soma(request, n_1, n_2):
    soma = n_1 + n_2
    return HttpResponse(f'<h1>A soma dos dois valores é: {soma}')

def subtrai(request, n_1, n_2):
    subtrai = n_1 - n_2
    return HttpResponse(f'<h1>A subtração dos dois valores é: {subtrai}')

def multiplica(request, n_1, n_2):
    multiplica = n_1 * n_2
    return HttpResponse(f'<h1>A multiplicação dos dois valores é: {multiplica}')

def divide(request, n_1, n_2):
    divide = n_1 + n_2
    return HttpResponse(f'<h1>A divisão dos dois valores é: {divide}')