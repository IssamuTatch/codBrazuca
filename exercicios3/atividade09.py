'''
Atividade 9: Ordenação de Números
Solicitação: Crie um programa que leia três números diferentes e os imprima em ordem
crescente.
Lógica: O programa precisa comparar os três números e ordená-los do menor para o maior.
Isso pode ser feito usando condições if-else para comparar cada par de números.
'''

def ordenar(lista):
    stop = False
    auxi = 0

    while stop != True:
        for i in range(len(lista)-1):
            if lista[0] <= lista[1] and lista[1] <= lista[2]:
                return lista
            elif lista[i] > lista[i+1]:
                auxi = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxi
        
        

lista = []

lista.append(float(input("Digite o primeiro número: ")))
lista.append(float(input("Digite o segundo número: ")))
lista.append(float(input("Digite o terceiro número: ")))

lista = ordenar(lista)

print("Lista em ordem crescente: ",lista)
