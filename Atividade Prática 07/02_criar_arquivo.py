#Criar arquivo

try:
    nome_arquivo = input("Digite o nome do arquivo (ex: pessoas.txt): ")

    quantidade = int(input("Quantas pessoas deseja cadastrar? "))

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        
        arquivo.write(f"{'Nome':<20}{'Idade':<10}{'Cidade':<20}\n")
        arquivo.write("-" * 50 + "\n")

        for i in range(quantidade):
            print(f"\nPessoa {i + 1}")
            nome = input("Nome: ")
            idade = input("Idade: ")
            cidade = input("Cidade: ")

            arquivo.write(f"{nome:<20}{idade:<10}{cidade:<20}\n")

    print("\nArquivo salvo com sucesso!")

except Exception as erro:
    print("Falha ao salvar o arquivo.")
    print("Erro:", erro)