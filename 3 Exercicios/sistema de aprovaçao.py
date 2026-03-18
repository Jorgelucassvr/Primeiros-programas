nota = float(input("qual a media final do aluno? "))
frequencia = int(input("qual a sua porcentagems de frequencia? ")) 

if frequencia>= 75 and nota >=60:
    print ("Aprovado direto")
elif nota<= 59 and nota>= 40:
    print ("Recuperaçao")
else:
    print("reprovado")