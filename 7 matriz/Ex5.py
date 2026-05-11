l = []
minimo = 0
maximo = 0
minimops = 0
maximops = 0
contador = -1
for _ in range(7):
    n = int(input("insira seu numero: "))
    l.append(n)
    if n > minimo and contador == -1:
        contador+=1
        minimo = n
    print (contador)
for n in l:
    if n > maximo:
        maximo = n 
        maximops = contador
    if n < minimo:
        minimo = n 
        minimops = contador
    contador += 1 
print("maior valor", maximo)
print("posiçao maior numero:", maximops)
print("menor valor", minimo)
print("posiçao menor numero:", minimops)