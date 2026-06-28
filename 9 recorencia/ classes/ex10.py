
def maior_elemento(valores, indice):
    if indice == len(valores) - 1:
        return valores[indice]

    maior_restante = maior_elemento(valores, indice + 1)

    if valores[indice] > maior_restante:
        return valores[indice]
    else:
        return maior_restante