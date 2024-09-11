'''
Atividade 19: Média Ponderada
Solicitação: Crie um programa que calcule a média ponderada de três notas fornecidas pelo
usuário, considerando os pesos 2, 3 e 5.
Lógica: A média ponderada é calculada multiplicando cada nota pelo seu peso, somando os
resultados, e dividindo pela soma dos pesos. O programa deve receber as notas e aplicar essa
fórmula.
'''

def media_ponderada(lista):
    return (lista[0]*2+lista[1]*3+lista[2]*5)/10

lista = []

lista.append(float(input("Digite o primeiro número: ")))
lista.append(float(input("Digite o segundo número: ")))
lista.append(float(input("Digite o terceiro número: ")))

print("Media Ponderada:",media_ponderada(lista))
