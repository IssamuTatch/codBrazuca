'''
Atividade 14: Calculadora Simples
Solicitação: Crie um programa que funcione como uma calculadora simples, pedindo ao
usuário dois números e a operação que deseja realizar.
Lógica: O programa deve pedir dois números e um operador (+, -, *, /). Dependendo do
operador fornecido, o programa deve executar a operação correspondente e exibir o resultado.
'''

def calculadora(numero1, operador, numero2 ):
     match operador:
        case "+":
            return str(numero1 + numero2)
        case "-":
            return str(numero1 - numero2)
        case "*":
            return str(numero1 * numero2)
        case "/":
            return str(numero1 / numero2)
        case default:
            return "ERRO"

numero1 = float(input("Digite o primeiro numero: "))
operador = str(input("digite o operador (+, -, *, /) :"))
numero2 = float(input("Digite o segundo numero: "))

print("Calculando...")
print("Resultado:",calculadora(numero1, operador, numero2))
