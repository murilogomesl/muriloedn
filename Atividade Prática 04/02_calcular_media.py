#Calcular média

def calcular_media_turma():
    total_notas = 0
    quantidade_alunos = int(input("Quantidade de alunos: "))

    for i in range(quantidade_alunos):
        nota = float(input(f"Digite a nota do aluno: {i + 1}: "))
        total_notas = total_notas + nota

    media = total_notas / quantidade_alunos
    print(f"Média da turma: {media:.2f}")

calcular_media_turma()
