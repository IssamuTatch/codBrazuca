'''
Atividade 10: Números Pares e Ímpares
Solicitação: Escreva um programa que peça ao usuário um número inteiro e informe se ele é
par ou ímpar.
Lógica: A paridade de um número pode ser determinada pelo resto da divisão do número por
2. Se o resto for 0, o número é par; se for 1, é ímpar.
'''

def impar_ou_par(numero):
    if numero % 2 == 0:
        print(numero, 'é par')
        return True
    elif numero % 2 != 0:
        print(numero, 'é ímpar')
        return False

numero = int(input("Digite um número: "))
impar_ou_par(numero)
