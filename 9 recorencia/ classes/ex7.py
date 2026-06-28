def existe(lista, valor, i):
    if i >= len(lista):
        return False
    if lista[i] == valor:
        return True
    return existe(lista, valor, i + 1)

list = [1,2,4,6,0]
if existe([1,2,4,6,1],1,3):
    print("verdade")

else:
    print("mentira")



 