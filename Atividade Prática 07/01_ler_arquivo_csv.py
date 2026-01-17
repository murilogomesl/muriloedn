#Ler arquivo

import pandas as pd

nome_arquivo = input("Digite o nome do arquivo CSV: ")

try:
    dados = pd.read_csv(nome_arquivo)

    media = dados["tempo_execucao"].mean()
    desvio_padrao = dados["tempo_execucao"].std()

    print("📊 Resultados:")
    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except KeyError:
    print("Erro: a coluna 'tempo_execucao' não existe no arquivo.")
except Exception:
    print("Erro ao ler o arquivo CSV.")