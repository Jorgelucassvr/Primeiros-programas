#escreve todos os numeros primos ate um numero
numero_max = int(input("Ate qual numero voce quer ver os numeros primos "))

for n in range(1,numero_max+ 1 ):
     print(n)
     nuemro_primo = n / n
     if nuemro_primo == 1:
      print(f"Numero {nuemro_primo} é primo")
     else:
        print(f"Numero {n} nao é primo")