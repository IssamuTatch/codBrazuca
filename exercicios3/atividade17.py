'''
Atividade 17: Verificação de Número Perfeito
Solicitação: Escreva um programa que verifique se um número dado é um número perfeito.
Lógica: Um número perfeito é um número que é igual à soma dos seus divisores próprios
(excluindo ele mesmo). O programa deve encontrar todos os divisores de um número e somálos para verificar essa condição.
'''

def numero_perfeito(numero):
    divisores = []
    for i in range(1 , round((numero/2)+1)):
        if numero % i == 0 and i != numero:
            divisores.append(i)
    if sum(divisores) == numero:
        return True

numero = int(input("Digite um número: "))

print("O número é perfeito") if numero_perfeito(numero) == True else print("O numero não é perfeito")