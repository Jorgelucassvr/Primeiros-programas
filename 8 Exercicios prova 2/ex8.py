lista = [(10,15),(11,25),(11,25),]
def distancia(cordenada1,cordenada2):
    cordenada1 = lista[0] 
    x = cordenada1[0]
    y = cordenada1[1]

    cordenada2= lista[1]
    x2 = cordenada2[0]
    y2 = cordenada2[1]

    resultado = ((((x2 - x)**2)+((y2-y)**2))**0.5)
    print (resultado)
    return resultado
cordenada1 = 1
cordenada2 = 2
resultado = distancia (cordenada1, cordenada2)
print (resultado)