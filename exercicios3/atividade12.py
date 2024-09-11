'''
Atividade 12: Jogo de Adivinhação
Solicitação: Crie um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o
usuário deve adivinhar qual é o número.
Lógica: O programa deve gerar um número aleatório e permitir que o usuário faça palpites,
dando dicas se o palpite foi maior ou menor que o número secreto, até que o usuário acerte.
'''

import random

resposta = random.randint(0, 100)

def jogo_adivinhar():
    print("Adivinhe o número")
    resposta = random.randint(0, 100)
    numero = -1
    while numero != resposta:
        numero = int(input("Digite um número: "))
        if numero < resposta:
            print("O número é maior")
        elif numero > resposta:
            print("O número é menor")
        else:
            print("Você acertou o número!!!")
            return

jogo_adivinhar()
