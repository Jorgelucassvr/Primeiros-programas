numeros = []
proximo = -1
contador = 0
cresente =False
falha = 0
for _ in range (8): 
    n = int(input("insira o numero: "))
    numeros.append(n)
    if contador == 0:
        proximo = n 
    contador+=1
for n in numeros:
    if n >= proximo and falha == 0:
        cresente = True
    else:
        falha +=1
        cresente = False
    proximo = n 
if cresente :
    print ("A lista esta em ordem cresente.")
else:
    print("A lista nao esta ordenada")