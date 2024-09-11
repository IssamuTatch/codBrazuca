'''
Atividade 7: Média de Notas
Solicitação: Desenvolva um programa que calcule a média de várias notas inseridas pelo
usuário. O programa deve parar de pedir notas quando o usuário digitar -1.
Lógica: O programa precisa coletar notas até que o usuário insira o valor -1. A cada nova nota,
você deve somá-la a um total acumulado e contar quantas notas foram inseridas. No final,
divida a soma total pelo número de notas para calcular a média.
'''

lista = []
stop = False
while stop != True:
    nota = float(input('Digite a nota ou digite "-1" para parar o programa: '))
    if nota != -1:
        lista.append(nota)
    else:
        stop = True

print("Média das nota: ", sum(lista)/len(lista))