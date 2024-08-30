'''
Atividade Prática:
Escreva uma função que receba um número e retorne se ele é par ou ímpar.
'''

# Retorna true para números pares e false para números ímpares
def impar_ou_par(numero):
    if numero % 2 == 0:
        print(numero, ' é par')
        return True
    if numero % 2 != 0:
        print(numero, ' é ímpar')
        return False

impar_ou_par(5)
impar_ou_par(10)