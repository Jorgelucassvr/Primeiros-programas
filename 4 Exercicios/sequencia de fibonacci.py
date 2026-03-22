print("Sequencia de fibonacci")
contador = int(input("Iinsira o numero de algarismos voce quer: "))
A = 0
B = 1
while contador >= 0:
    
    print(f"{A}") 

    proximo = A + B
    A = B
    B = proximo 
    contador = contador - 1