numero  = int(input("insira o seu numero: "))
fatorial = 1
while numero > 0:
    fatorial = fatorial * numero 
    numero = numero - 1
print(f"seu resultado é {fatorial}")