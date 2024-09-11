'''
Atividade 2: Conversão de Temperaturas
Solicitação: Crie um programa que converta uma temperatura dada em Celsius para Fahrenheit
e Kelvin.
Lógica: A conversão de temperaturas segue fórmulas matemáticas específicas. Para converter
de Celsius para Fahrenheit, você deve usar a fórmula (C * 9/5) + 32. Para converter de Celsius
para Kelvin, a fórmula é C + 273.15. O programa deve pedir a temperatura em Celsius e realizar
as conversões.
'''

def C_to_F(celsius):
    temperatura = (celsius * 9/5)+32
    return temperatura    

def C_to_K(celsius):
    temperatura = celsius + 273.15
    return temperatura

temperatura = float(input("Digite a temperatura em Celsius: "))

print("Fahrenheit:",C_to_F(temperatura))
print("Kelvin:",C_to_K(temperatura))
