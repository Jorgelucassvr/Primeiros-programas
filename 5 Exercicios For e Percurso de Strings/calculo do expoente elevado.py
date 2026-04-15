base = int(input("  insira seu numero: "))
expoente = int(input("insira seu expoente: "))
resultado = 1 
if expoente < 0 or base < 0:
    print ("valor invalido")
else:
    for _ in range (expoente):
       resultado *= base 
    print(f"{base} ^ {expoente} = {resultado}")