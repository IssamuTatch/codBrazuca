'''
Atividade 6: Contagem de Vogais
Solicitação: Crie um programa que peça uma frase ao usuário e conte quantas vogais (a, e, i, o,
u) ela contém.
Lógica: O programa deve percorrer cada letra da frase e verificar se é uma vogal. Você pode
fazer isso usando um loop e uma condição para verificar se a letra pertence ao conjunto de
vogais.
'''

def contador_vogais(frase):
    count = 0
    for elements in frase:
        if elements.lower() == "a" or  elements.lower() == "e" or  elements.lower() ==  "i" or elements.lower() ==  "o" or elements.lower() ==  "u":
            count = count + 1
    return count

frase = str(input("Digite uma frase: "))

print("A frase tem ",contador_vogais(frase), "vogais")