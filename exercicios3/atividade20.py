'''
Atividade 20: Análise de Lista de Números
Solicitação: Escreva um programa que peça ao usuário uma lista de números e, ao final, exiba o
maior, o menor, e a média dos números inseridos.
Lógica: O programa deve permitir que o usuário insira vários números, armazenando-os em
uma lista. Após a entrada de todos os números, o programa deve calcular e exibir o maior, o
menor e a média dos valores.
'''

def min_max(lista):
    min = 999999999999999999999 #tendendo a infinito
    max = 0
    if len(lista) > 1:
        for numero in lista:
            if numero > max:
                max = numero
            if numero < min:
                min = numero
        print("Min: ", min)
        print("Max: ", max)
    elif len(lista) > 0:
        min = lista[0]
        max = lista[0]
        print("Min: ", min)
        print("Max: ", max)
    else:
        print("Lista Vazia")

def media(lista):
    if len(lista) > 0:
        print("Media", sum(lista)/len(lista))
    else: 
        print("Lista vazia")

lista = []

stop = False

while stop != True:
    numero = float(input('Digite um número "-1" para parar: '))
    if numero != -1:
        lista.append(float(numero))
    else:
        stop = True

media(lista)

min_max(lista)