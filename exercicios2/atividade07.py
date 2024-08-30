'''
Atividade Prática:
Crie uma lista de compras que permita ao usuário adicionar itens e, em seguida,
imprimir a lista completa.
'''

list = []

item = ""

print('Digite um item para adicionar na lista. Digite "QUIT" para imprimir a lista')

while item.casefold() != "QUIT".casefold():
    item = input("Digite um Item: ")
    if not item.casefold()  == 'QUIT'.casefold() and not item  == '':
        list.append(item.upper())

print(list)