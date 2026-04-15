id_francisca = 0
idade_1, idade_2, idade_3 = 0,0,0
rep = 1
while rep <= 3:
    idade = int(input("insira a idade"))
    if idade > 0 and idade_1 == 0:
        idade_1 = idade
    elif idade > 0 and idade_2 == 0:
        idade_2 = idade
    elif idade > 0 and idade_3 == 0:
        idade_3= idade
    rep+= 1
if (idade_1 > idade_2 and idade_1 < idade_3) or (idade_1 < idade_2) and (idade_1> idade_3):
    id_francisca = idade_1
elif (idade_2 > idade_1 and idade_2 < idade_3) or (idade_2 < idade_1) and (idade_2> idade_3):
    id_francisca = idade_2
else:
    id_francisca = idade_3
print(id_francisca)