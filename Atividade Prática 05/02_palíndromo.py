#Teste de palíndromo

def verificar_palindromo(texto):
    texto_limpo = ""

    for caractere in texto.lower():
        if caractere.isalnum():
            texto_limpo += caractere

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


frase = input("Digite uma palavra ou frase: ")
print(verificar_palindromo(frase))
