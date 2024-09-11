'''
Atividade 5: Tabuada
Solicitação: Escreva um programa que exiba a tabuada de um número fornecido pelo usuário.
Lógica: Para gerar a tabuada de um número, você deve multiplicar o número por cada valor de
1 a 10. O programa deve iterar de 1 a 10, multiplicando o número fornecido e exibindo os
resultados.
'''

def tabuada(numero, range):
    if range > 0:
        print(numero, "X", range, "=", numero*range)
        tabuada(numero, range - 1)
    

numero = int(input("Digite um numero inteiro: "))

tabuada(numero, 10)

