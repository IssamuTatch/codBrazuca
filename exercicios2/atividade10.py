'''
Atividade Prática:
Crie um programa que encontre e imprima todos os números primos em um intervalo
definido pelo usuário.
'''

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

limiteMinimo = int(input('Limite Minimo: '))

limiteMaximo = int(input('Limite Maximo: '))

for numero in range(limiteMinimo, limiteMaximo+1):
    if eh_primo(numero):
        print(numero)