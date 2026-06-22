def contar_digitos(n):  
    if n == 0:
        return 1
    contagem = 0
    while n > 0:
        n = n // 10
        print(n)
        contagem += 1
    return contagem
n = int(input("insira o numero: "))
resultado = contar_digitos(n) 
print (resultado)