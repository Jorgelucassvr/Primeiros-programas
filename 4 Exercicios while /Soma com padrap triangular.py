contador = 1
soma = 0
n = int(input("insira o numero: "))

print("S = ")

while contador <= n:

    denominador = contador * (contador + 1) // 2
    termo = contador / denominador

    soma = soma + termo

    print(f"{contador} / {denominador}")

    contador = contador + 1

print(f"Resultado = {soma}")