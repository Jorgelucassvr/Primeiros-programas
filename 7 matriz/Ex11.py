numeros = []
numeros_contra = []
palindromo = True
for _ in range (7):
    n = int(input("insira o numero: "))
    numeros.append(n)
for n in range (len(numeros)-1,-1,-1):
    p = (numeros[n])
    numeros_contra.append(p)
    print (numeros,numeros_contra)
if numeros_contra != numeros:
    palindromo = False
if palindromo :
    print ("A lista é um palindromo")
else:
    print("A lista nao é um palindromo")
