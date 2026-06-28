def ocorrencia(numeros, apartir, comparador):
    if apartir == len(numeros):
        return 0
    if numeros[apartir] == comparador:
        return 1 + ocorrencia(numeros, apartir + 1, comparador)
    return ocorrencia(numeros, apartir + 1, comparador)
valores = [4, 7, 4, 2, 4, 9]
print(ocorrencia(valores, 0,4))