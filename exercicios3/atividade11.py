'''
Atividade 11: Cálculo de Área de Círculo
Solicitação: Desenvolva um programa que calcule a área de um círculo a partir do raio
fornecido pelo usuário.
Lógica: A fórmula da área de um círculo é A = πr², onde r é o raio do círculo. O programa deve
pedir o raio, aplicar a fórmula e exibir o resultado.
'''

def area_circulo(r):
    pi = 3.141592653589793
    a = pi*r**2
    return a

raio = float(input("Digite o raio do circulo: "))

print("A area do circulo:",area_circulo(raio))
