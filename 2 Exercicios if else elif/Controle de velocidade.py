#Considere que o limite de velocidade em uma avenida seja 60 km/h. 
# Se o veículo estiver até o limite, considera-se que está dentro da velocidade permitida.
# Se estiver acima do limite,
# até 20 km/h acima, o sistema registra excesso de velocidade. 
# Caso a velocidade seja mais de 20 km/h acima do limite, o sistema registra excesso grave de velocidade.

#Radar
Velocidade = float(input("Qual e a velocidade do veiculo em Km/hr: "))

Resultado_velocidade = Velocidade - 60 

if Resultado_velocidade > 20:
 velocidade_final = ("Ouve um execesso grave de velocidade")
elif Resultado_velocidade > 0:
  velocidade_final = ("Ouve um execesso de velocidade ")
elif Resultado_velocidade > -59:
  velocidade_final = ("Velocidade esta dentro do limite")
else: 
  velocidade_final = ("Velocidade foi Invalida")
print(f"\n.\n.\n. --------------------\n     Radar informa que:\n {velocidade_final}\n--------------------\n.\n.\n. ")