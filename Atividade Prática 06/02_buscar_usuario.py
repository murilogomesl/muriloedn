#Busca de usuário

import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()  # gera erro se a resposta não for 200

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Usuário gerado com sucesso:")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except requests.exceptions.RequestException:
    print("Falha ao conectar à API. Tente novamente mais tarde.")