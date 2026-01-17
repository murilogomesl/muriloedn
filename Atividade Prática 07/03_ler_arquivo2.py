#Lê arquivo

try:
    nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())

except FileNotFoundError:
    print("Erro: o arquivo não foi encontrado.")

except Exception as erro:
    print("Erro ao ler o arquivo.")
    print("Detalhes:", erro)