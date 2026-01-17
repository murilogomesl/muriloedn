#Consultar CEP

import requests

cep = input("Digite o CEP (apenas números): ").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()

    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("📍 Endereço encontrado:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

except requests.exceptions.RequestException:
    print("Falha ao consultar o CEP.")