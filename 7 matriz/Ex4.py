list_inicial = []
for _ in range (8):
    palavras = input("insira a palavra:")
    list_inicial.append(palavras)
for palavras in range ( len(list_inicial)-1,-1,-1):
    print (list_inicial[palavras])