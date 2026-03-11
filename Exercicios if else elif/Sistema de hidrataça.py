#Se a pessoa consumiu menos de 1 litro de água, o nível é considerado baixo. 
#Se consumiu entre 1 e 2 litros, o nível é considerado adequado.
#Consumo de mais de 2 litros nível é considerado alto.
 
Agua_consumida = float(input("Quantos litros de agua foram consumidos hoje? "))
if Agua_consumida > 2 :
 Resultado_da_agua = ("Muito alto")

elif Agua_consumida >= 1:
 Resultado_da_agua = ("Adequado")

elif Agua_consumida >0 :
 Resultado_da_agua = ("Baixo")

else:
 Resultado_da_agua = ("Invalido")

print(f" \n.\n.\n.\n---------------------\nTotal de consumo:\n    {Resultado_da_agua}\n---------------------\n.\n.\n.")