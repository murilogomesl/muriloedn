#Calcular preço final

preco_original = float(input("Digite o preço do produto: R$ "))
desconto_percentual = float(input("Digite o desconto (%): "))

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")