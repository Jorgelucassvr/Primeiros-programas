contador = 1
soma = 0

n = int(input("insira o numero: "))

print("S = 1")

while contador <= n:
    termo = 1 / contador

    if contador == 1:
        soma = 1
    else:
        if contador % 2 == 0:
            soma = soma - termo
            print("-", "1/" + str(contador))
        else:
            soma = soma + termo
            print("+", "1/" + str(contador))

    contador = contador + 1

print("Resultado =", soma)