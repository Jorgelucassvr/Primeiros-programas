n = int(input("insira o numero: "))
fatorial = 1
numerador = 0
resultado = 0
for i in range (1, n+1):
    fatorial *= i
    numerador += i 
    resultado += (numerador * fatorial) / fatorial
print(resultado)
