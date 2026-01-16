#Conversor de Temperatura

temperatura = float (input("Digite a temperatura:"))
inicial = input("Unidade inicial (C, F, K):").upper()
final = input("Unidade final (C, F, K): ").upper()

if inicial == "C" and final == "F":
    resultado = (temperatura * 9/5) + 32

elif inicial == "C" and final == "K":
    resultado = temperatura + 273.15

elif inicial == "F" and final == "C":
    resultado = (temperatura - 32) * 5/9

elif inicial == "F" and final == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15

elif inicial == "K" and final == "C":
    resultado = temperatura - 273.15

elif inicial == "K" and final == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32

elif inicial == final:
    resultado = temperatura

else:
    print("Unidade inválida")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado:.2f}°{final}")