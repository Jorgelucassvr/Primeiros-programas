
contador = 0
notas = 0
prova = 5
while prova >= 1:
     nota = int(input(f"insira a nota da prova {prova}: "))
     contador = contador + nota 
     prova = prova - 1
contador = contador / 5 
print(f"a media das provas  = {contador}")
