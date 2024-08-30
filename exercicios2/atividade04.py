'''
Atividade Prática:
Escreva um programa que peça a temperatura atual e diga se está quente (acima de
30°C), frio (abaixo de 15°C) ou agradável (entre 15°C e 30°C).
'''

temperatura = float(input("Qual a temperatura atual? \n"))

if temperatura >= 30:
    print("Está quente")
elif temperatura <30 and temperatura > 15:
    print("Está agradavel")
else:
    print("Está frio")