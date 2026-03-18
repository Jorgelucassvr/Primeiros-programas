pontuacao = float(input("pontuaçao obtida: "))
tempo_gasto = int(input("tempo gato em(min) "))

if pontuacao >= 90:
    print ("ouro")
elif pontuacao >= 70:
    print ("prata")
elif pontuacao >= 50:
    print ("bronze")
else:
    print("sem medalha")
if pontuacao>= 90 and tempo_gasto<120:
    print ("Participante destaque da competicao")