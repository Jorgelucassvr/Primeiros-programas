resultado,resultado_1,resultado_2 = 0,1,0
n=int(input("insira o numero "))
contador = 1
while n >= contador:
    resultado_1 *= (contador + 1)
    resultado_2 = contador ** 2

    resultado += resultado_1 / resultado_2

    contador += 1
print ("resultado e ", resultado)

 