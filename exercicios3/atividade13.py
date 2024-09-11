'''
Atividade 13: Soma de Números Pares
Solicitação: Escreva um programa que calcule a soma de todos os números pares entre 1 e
100.
Lógica: Para somar todos os números pares entre 1 e 100, o programa deve iterar por esses
números, verificando se cada um é par (divisível por 2) e, se for, adicioná-lo a uma soma
acumulada.
'''

def sum_par(max):
    soma = 0
    for numero in range(max+1):
        if numero % 2 == 0:
            soma = soma + numero
    return soma

max = 100

print("Soma:", sum_par(100))