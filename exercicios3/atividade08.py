'''
Atividade 8: Sequência de Fibonacci
Solicitação: Escreva um programa que mostre os primeiros n números da sequência de
Fibonacci, onde n é informado pelo usuário.
Lógica: A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos
dois anteriores. O programa deve gerar a sequência até o enésimo termo solicitado pelo
usuário.
'''
lista = [0, 1]

def fibonacci(n):

    if n == 0:
        return ""
    if n == 1:
        return lista[0]
    elif n == 2:
        return lista
    else:
        for i in range(n-2):
            lista.append(lista[-1]+lista[-2])
        return(lista)


numero = int(input("Digite um número: "))
print(fibonacci(numero))
