n = int(input("insira um numero "))
resultado_1, resultado_2, resultado = 1,1,0
contador_1 = 1

for contador in range( 1, n+1 ):

    resultado_1 *= contador_1 

    resultado_2 = ( 2 ** contador) * contador
    
    resultado += resultado_1 / resultado_2

    contador_1 += 2

print(resultado)
