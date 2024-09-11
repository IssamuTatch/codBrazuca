'''
Atividade 15: Soma dos N primeiros Números
Solicitação: Escreva um programa que peça ao usuário um número n e calcule a soma dos
primeiros n números naturais.
Lógica: A soma dos primeiros n números naturais pode ser encontrada usando a fórmula da
soma de uma progressão aritmética ou iterando de 1 até n e acumulando a soma.
'''

def sum(max):
    soma = 0
    for numero in range(max+1):
        soma = soma + numero
    return soma

n = int(input("Digite até qual número deve ser somado: "))

print("Soma dos números naturais:", sum(n))
