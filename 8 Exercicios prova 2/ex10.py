paragrafo = input("insira seu paragrafo: ")
paragrafo.lower()
paragrafo.replace(",","")
paragrafo.replace(".","")
lista= []
contagem ={}
for i in paragrafo.split():
    lista.append(i)
for palavra in lista:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
ordenado = sorted(contagem, key=lambda x: contagem[x], reverse=True)

top3 = ordenado[:3]
print(top3)