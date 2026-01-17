
pares = 0
impares = 0

quantidade = int(input("Quantos números você vai digitar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))

    if numero % 2 == 0:
        print("Número par")
        pares += 1
    else:
        print("Número ímpar")
        impares += 1

print("\nResultado final:")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
