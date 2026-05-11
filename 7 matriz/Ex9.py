temperatura_atual = 0
temperatura = float(input("insira a temperatura: "))
temperatura_atual = temperatura
aumentou = 0
diminuiu = 0
igual = 0
for _ in range (9):
    temperatura = float(input("insira a temperatura: "))
    if temperatura_atual < temperatura:
        aumentou+=1
    elif temperatura_atual == temperatura:
        igual+= 1
    else:
        diminuiu+=1

    temperatura_atual = temperatura
print("aumentou:",aumentou)
print("diminuiu:",diminuiu)
print("permaneceu igual:",igual)