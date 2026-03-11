#soma das notas - 
# media - 
# pontos para media maxima 
#cada prova vale 10 pontos 
nota_1= float(input("qual a nota da primeira prova ? ")) 
nota_2= float(input("qual a nota da segunda prova ? "))
nota_3= float(input("qual a nota da segunda prova ? "))
total_de_pontos = nota_1 + nota_2 + nota_3
media = total_de_pontos / 3 
pontos_maximos_para_media = 10 - media

print(f"RELATORIO DE NOTAS")
print(f"Total de notas = {total_de_pontos: .1f}")
print(f"Media do aluno = {media: .2f}")
print(f"Pontos que faltam para meida ={pontos_maximos_para_media}")