temperatura = float(input("insira a temperatura: "))
if temperatura < 10 and temperatura >= 0:
    print ("Temperatura baixa")
elif temperatura >= 10 and temperatura <= 25:
    print("Temperatura agradavel")
elif temperatura > 25:
    print("Temperatura alta")
else:
    print("Valor invalido")