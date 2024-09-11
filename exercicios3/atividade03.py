'''
Atividade 3: Cálculo de IMC
Solicitação: Escreva um programa que peça o peso e a altura de uma pessoa e calcule seu
Índice de Massa Corporal (IMC).
Lógica: O IMC é calculado dividindo o peso de uma pessoa em quilogramas pelo quadrado da
sua altura em metros. O programa deve receber esses dois valores, aplicar a fórmula IMC =
peso / (altura * altura) e exibir o resultado.
'''

def IMC(peso, altura):
    imc = peso/altura**2
    return imc

peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

print("IMC:",IMC(peso, altura))
