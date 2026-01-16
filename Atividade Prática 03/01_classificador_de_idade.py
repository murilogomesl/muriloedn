#Classificador de idade

idade = int (input("Digite sua idade:"))

if idade < 0:
    print("Idade Inválida")
elif idade <=12:
    print("Criança")
elif idade <=17:
    print("Adolescente")
elif idade <=59:
    print("Adulto")
else:
    print("Idoso")