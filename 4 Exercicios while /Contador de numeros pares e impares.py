
numero_p_verificar = 0
contagem_par = 0 
contagem_impar = 0
numero = 10
while numero >= 1:
     numero_p_verificar = int(input(f"escreva o numero {numero}: " ))
     numero_verificado = numero_p_verificar % 2 
     if numero_verificado == 1:
          contagem_impar = contagem_impar + 1
     else:
          contagem_par = contagem_par  + 1

     numero = numero - 1 
print(f" numeros impares foram: {contagem_impar} \n numeros pares foram: {contagem_par}")