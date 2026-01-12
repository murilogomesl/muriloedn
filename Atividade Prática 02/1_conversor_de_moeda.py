#Conversor de Moeda

valor_reais = 100
taxa_dolar = 5.20
taxa_euro = 6.15

conversao_dolar = valor_reais / taxa_dolar
conversao_euro = valor_reais / taxa_euro

print(f"Valor em reais: R${valor_reais:.2f}")
print(f"Taxa do dólar: US${taxa_dolar:.2f}")
print(f"Taxa do euro: €{taxa_euro:.2f}")
print()
print(f"Conversão de reais para dólar: US${conversao_dolar:.2f}")
print(f"Conversão de reais para euro: €{conversao_euro:.2f}")