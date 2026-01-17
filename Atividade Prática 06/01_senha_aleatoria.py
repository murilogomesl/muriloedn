#Senha aleatória

import random
import string

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print(f"Senha gerada: {senha}")