list_inicial = []
par = 0 
impares = 0
list_pares = []
list_impares = []
for _ in range(10):
    n = int(input("insira os numeros: "))
    list_inicial.append(n)
for numero in list_inicial:
    if numero % 2 == 0:
        par+=1
        list_pares.append(numero)
    else:
        impares+=1
        list_impares.append(numero)
print("impares =", impares)
print("lista =",list_impares)
print("impares =", par )
print("lista =",list_pares)