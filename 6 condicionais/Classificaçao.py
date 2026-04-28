

#       Para cada número i no intervalo de A até B, o programa deve
#       mostrar o número i
#       mostrar todos os números de 1 até i
#       indicar, para cada valor, se ele é
#       múltiplo de 3
#       múltiplo de 5
#       múltiplo de ambos
#       ou nenhum dos dois


inicio = int(input("isira o inicio: "))
final = int(input("insira o final: "))
for i in range (inicio, final+1):
    if i  % 5 ==0 and i % 3 ==0 :
        print(f"{i} - é divisor de ambos")
    elif i  % 5 ==0 :
        print(f"{i} - é divisor de 5")
    elif i  % 3 ==0:
        print(f"{i} - é divisor de 3")
    else:
        print(f"{i}")



