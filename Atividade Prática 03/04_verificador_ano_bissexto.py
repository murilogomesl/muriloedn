#Verificador de ano bissexto

ano = input("Digite um ano: ")

if not ano.isdigit() or len(ano) != 4:
    print("Ano inválido")
else:
    ano = int(ano)

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto")
    else:
        print(f"{ano} não é um ano bissexto")