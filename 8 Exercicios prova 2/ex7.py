matriz = [
    [1, 2, 3, 4, 5, 6,],
    [1, 2, 3, 4, 5, 6,],
    [1, 2, 3, 4, 5, 6,],
    [1, 2, 3, 4, 5, 6,],
    [1, 2, 3, 4, 5, 6,],
    [1, 2, 3, 4, 5, 6,],
]
matriz_equilibrada =[
]
lista = []
for linha in  range (1, len(matriz)-1):
    for elemento in range (2,len(matriz)):
        print(elemento)
        media = (elemento+elemento+elemento+(elemento+1)+(elemento-1))/5
        lista.append(media)
        if len(lista) == 4:
            matriz_equilibrada.append(lista)
            lista = []
print(matriz_equilibrada)