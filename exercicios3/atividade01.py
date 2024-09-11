'''
Atividade 1: Calculando o Fatorial
Solicitação: Escreva um programa que peça um número inteiro ao usuário e calcule o fatorial
desse número.
Lógica: O fatorial de um número é o produto de todos os números inteiros positivos menores
ou iguais a ele. Por exemplo, o fatorial de 5 (escrito como 5!) é 5 * 4 * 3 * 2 * 1. Você precisará
usar um loop que multiplique o número pelo seu antecessor até chegar a 1.
'''

def fatorial(numero):
    if numero > 1:
        result = numero * fatorial(numero - 1)
        return result
    else:
        result = 1
        return result

numero = int(input("Digite um número: "))
print("Fatorial:",fatorial(numero))
