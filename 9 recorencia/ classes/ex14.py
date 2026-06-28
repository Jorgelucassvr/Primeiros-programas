def compactar_texto(texto, indice, caractere_atual, quantidade):
    if texto == "":
        return  ""
    if indice == len(texto):
        return caractere_atual + str(quantidade)
    if caractere_atual == "":
        return compactar_texto(texto, indice + 1, texto[indice], 1)
    if texto[indice] == caractere_atual:
        return compactar_texto(texto, indice + 1 ,caractere_atual,quantidade+1)
    return caractere_atual + str(quantidade) + compactar_texto(texto, indice + 1, texto[indice], 1)
texto = input("Digite o texto: ")
print(compactar_texto(texto, 0, "", 0))

