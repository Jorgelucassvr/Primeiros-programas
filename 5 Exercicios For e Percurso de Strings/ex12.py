n = int(input("insira um numero: "))


for linha in range(1, n + 1):

    for numero in range(1, linha + 1):

        print(numero, end=" ")
    print()

for linha in range(n - 1, 0, -1):


    for numero in range(1, linha + 1):

        print(numero, end=" ")
    print()
