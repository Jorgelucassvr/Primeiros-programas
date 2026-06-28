labirinto = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [3, 0, 0, 0, 1, 0, 0, 0, 1, 1]
]

def encontrar_saida(labirinto, linha, coluna):
    if linha < 0 or linha >= len(labirinto):
        return False
    if coluna < 0 or coluna >= len(labirinto[0]):
        return False

    if labirinto[linha][coluna] == 1:
        return False

    if labirinto[linha][coluna] == 2:
        return False

    if labirinto[linha][coluna] == 4:
        print("encontrou a saída")
        return True

    if labirinto[linha][coluna] != 3:
        labirinto[linha][coluna] = 2

    if encontrar_saida(labirinto, linha, coluna + 1):
        return True

    if encontrar_saida(labirinto, linha + 1, coluna):
        return True

    if encontrar_saida(labirinto, linha, coluna - 1):
        return True

    if encontrar_saida(labirinto, linha - 1, coluna):
        return True

    return False


print(encontrar_saida(labirinto, 0, 0))