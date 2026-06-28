def calcular_mdc(a, b):
    if b == 0:
        return a
    return calcular_mdc(b, a % b)

while True:
    a = int(input("Digite o primeiro número (0 para sair): "))

    if a == 0:
        break

    b = int(input("Digite o segundo número: "))

    mdc = calcular_mdc(a, b)
    mmc = (a * b) // mdc

    print("MDC:", mdc)

    if mdc == 1:
        print("São coprimos: sim")
    else:
        print("São coprimos: não")

    print("MMC:", mmc)
    print()