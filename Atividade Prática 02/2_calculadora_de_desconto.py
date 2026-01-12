#Calculadora de desconto

nome_produto = "camiseta"
preco = 50.00
desconto = 20

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print("Produto:", nome_produto)
print(f"Preço: R${preco:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Preço final: R${preco_final:.2f}")
