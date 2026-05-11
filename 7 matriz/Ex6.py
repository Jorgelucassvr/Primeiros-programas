notas = []
total = 0
alunos_acima = 0
notas_acima = []
for _ in range (10):
    n = int(input("insira as notas: "))
    notas.append(n)
    total += n 
media = total/ len(notas)
for nota in notas:
    if nota > media:
        alunos_acima+=1
        notas_acima.append(nota)
print(f"A media da turma é: {media}\nQuantidade de notas acima da media: {alunos_acima}\nNotas acima da media: {notas_acima}")
