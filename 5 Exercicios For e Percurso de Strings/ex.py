
n = int(input("insira o numero: "))
q = "0"
w = "1"
fila_atual = 1
meio = ""
m = n-1
for _ in range (0, n):
    if fila_atual ==1:
        for _ in range (0, n):
            print (w, end ="")
        print()
    elif fila_atual < n :
        for i in range (1, m):
            meio += q
        print(w + meio + w)
        meio = ""         
    else:
        for _ in range (0, n):
            print (w, end ="")
        print()
    fila_atual +=1
    