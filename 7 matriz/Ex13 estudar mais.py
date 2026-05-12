numeros = []
for i in range(10):
    n = int(input("Digite um número: "))
    numeros.append(n)
maior = numeros[0]
segundo_maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
existe = False
for n in numeros:
    if n != maior:
        if existe == False:
            segundo_maior = n
            existe = True

        elif n > segundo_maior:
            segundo_maior = n

if existe:
    print("Maior valor:", maior)
    print("Segundo maior valor:", segundo_maior)
else:
    print("Não existe segundo maior valor distinto.")
    