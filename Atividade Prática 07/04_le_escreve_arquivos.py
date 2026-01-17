#Lê e escreve arquivos

import json

try:
    nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ")

    # Coletando os dados
    pessoa = {
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "cidade": input("Cidade: ")
    }

    # Salvando no arquivo JSON
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print("\nDados salvos com sucesso!\n")

    # Lendo o arquivo JSON
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("Dados lidos do arquivo:")
    print(f"Nome: {dados_lidos['nome']}")
    print(f"Idade: {dados_lidos['idade']}")
    print(f"Cidade: {dados_lidos['cidade']}")

except FileNotFoundError:
    print("Erro: o arquivo não foi encontrado.")

except Exception as erro:
    print("Falha ao salvar ou ler o arquivo.")
    print("Detalhes:", erro)