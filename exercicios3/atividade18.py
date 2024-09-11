'''
Atividade 18: Contagem de Palavras
Solicitação: Desenvolva um programa que conte quantas palavras há em uma frase fornecida
pelo usuário.
Lógica: O programa deve dividir a frase em palavras usando espaços como delimitadores e
contar quantas palavras resultaram dessa divisão.
'''

def contar_palavras(frase):
    notEmpty = False
    if frase == "":
        return 0
    listaPalavras = []
    palavra = ""
    for i in frase:
        if i != " ":
            palavra = palavra + i
            notEmpty = True
        else:
            if palavra != "":
                listaPalavras.append(palavra)
                palavra = ""
    if notEmpty == True:
        return len(listaPalavras)+1
    else: 
        return 0

frase = str(input("Digite uma frase: "))
print("Essa frase tem", contar_palavras(frase), "palavras")