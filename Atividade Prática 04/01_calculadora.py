#Calculadora de operações básicas

def calculadora():

    calculo = input("Selecione a operação (+, -, *, /):")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if calculo == "+":
        resultado = num1 + num2
    elif calculo == "-":
        resultado = num1 - num2
    elif calculo == "*":
        resultado = num1 * num2
    elif calculo == "/":
        resultado = num1 / num2
    else:
        print("Cálculo inválido")
        
    
    print(f"Resultado: {resultado}")

calculadora()