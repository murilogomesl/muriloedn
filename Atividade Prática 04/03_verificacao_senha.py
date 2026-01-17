#Verificador de senha

def verificar_senha():
    senha = input("Digite sua senha:")

    if len(senha) < 8:
        print("Senha inválida: deve ter pelo menos 8 caracteres.")
        return

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True

    if tem_numero:
        print("Senha válida.")
    else:
        print("Senha inválida: deve conter pelo menos um número.")

verificar_senha()
    