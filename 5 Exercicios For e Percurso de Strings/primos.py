n = int (input("insira o numero: "))
contador = 2 
while contador < n :
    if n % contador == 0:
        primo = False
        break
    else: 
        primo = True
    contador += 1
if primo :
    print ("é primo")
else:
    print ("nao e primo ")