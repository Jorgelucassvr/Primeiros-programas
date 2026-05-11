lista_inicial = []
lista_ajustada = []
for _ in range (8):
    preço = int(input("insira os prços: "))
    lista_inicial.append(preço)
    if preço<100:
        preço = preço * 1.10
    else:
        preço = preço * 1.05
    lista_ajustada.append(preço)
print("lista inicial", lista_inicial)
print("lista ajustada", lista_ajustada)