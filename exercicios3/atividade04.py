'''
Atividade 4: Verificação de Palíndromo
Solicitação: Crie um programa que verifique se uma palavra ou frase é um palíndromo.
Lógica: Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma de trás para
frente. O programa deve comparar a string original com sua versão invertida. Se forem iguais, é
um palíndromo; caso contrário, não é.
'''

def palindromo(palavra):
    invertida = palavra[::-1]
    if invertida.casefold() == palavra.casefold():
        return True
    else:
        return False

palavra = str(input("Digite uma palavra: "))

if palindromo(palavra) == True:
    print("Essa palavra é um palindromo")
else:
    print("Essa palavra não é um palindromo")
