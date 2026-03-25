contagem = 8
menor_numero = 0
maior_numero = 0
while contagem >= 1:
     numero = int(input(f"escreva o valor de {contagem}: "))

     contagem = contagem - 1 
     if numero > maior_numero:
      maior_numero = numero 
     if numero < menor_numero or menor_numero == 0:
        menor_numero = numero


      
print(f"menor numero foi: {menor_numero} \nmaior numero foi: {maior_numero}")