'''
Atividade Prática:
Escreva um programa que peça uma frase ao usuário e conte quantas vezes uma letra
específica aparece.
'''

result = 0
index = []

frase = input('Digite uma frase, para ver quantas vezes os caracteres aparecem nela.\n ')

for char in frase:
    if len(index) != 0:
        for i in range(len(index)):
            if char.upper() != index[i][0]:
                if i == len(index)-1:
                    index.append([char.upper(), 1])
                    break
            elif char.upper() == index[i][0]:
                index[i][1] = index[i][1] + 1
                break
    else:
        index.append([char.upper(), 1])

for i in index:
    print('"{}" apareceu {} vezes'. format(i[0], i[1]))