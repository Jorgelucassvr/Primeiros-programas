horas = int(input("insira as horas: "))
total = 0
if horas <= 100:
    total = horas * 5 
elif horas <= 500:
    total = (100 * 5) + (horas - 100) * 4
else:
    total = (100 * 5) + (400 * 4) + (horas - 500) * 2.5

print("R$",total)  