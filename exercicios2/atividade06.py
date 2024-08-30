'''
Atividade Prática:
Crie um programa que pergunte ao usuário por números até que ele digite zero e
então mostre a soma dos números digitados.
'''

print('Digite os números para somar. Quando digitar "0" será mostrado o resultado da soma')

numero = 1
soma = 0

while numero != 0:
    numero = float(input('Digite o número: '))
    soma = soma + numero

print("O valor da soma: ", soma)