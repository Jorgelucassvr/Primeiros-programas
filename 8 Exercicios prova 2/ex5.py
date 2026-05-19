
horas = 800
def calcular_horas (horas):
    total = 0
    for h in range (1 , horas+1):
        if h<=100:
            total += 5
        elif h <= 500:
            total += 4
        elif h > 500:
            total += 2.50
    print(total)
    return total

calcular_horas(horas)

