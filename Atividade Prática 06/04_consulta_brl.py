#Consultar BRL

import requests
from datetime import datetime

moeda = input("Digite a moeda (ex: USD, EUR, BTC): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()

    dados = resposta.json()

    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        cotacao = dados[chave]

        valor_atual = cotacao["bid"]
        maxima = cotacao["high"]
        minima = cotacao["low"]

        data_hora = datetime.fromtimestamp(
            int(cotacao["timestamp"])
        ).strftime("%d/%m/%Y %H:%M:%S")

        print("💰 Cotação encontrada:")
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {valor_atual}")
        print(f"Máxima do dia: R$ {maxima}")
        print(f"Mínima do dia: R$ {minima}")
        print(f"Última atualização: {data_hora}")

except requests.exceptions.RequestException:
    print("Erro ao consultar a cotação. Verifique a moeda ou sua conexão.")