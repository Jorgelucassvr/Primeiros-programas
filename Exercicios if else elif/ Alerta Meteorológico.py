#Um sistema de monitoramento climático emite alertas quando determinadas

#condições atmosféricas podem representar riscos para a população.

# Um alerta deve ser emitido quando a velocidade do vento for maior que 60 km/h 

# e a quantidade de chuva prevista for maior que 50 mm.

#Caso as duas condições ocorram simultaneamente, o sistema deve indicar alerta de tempestade. 

# Caso contrário, o sistema deve informar que não há alerta meteorológico.

#Escreva um programa que determine se um alerta deve ser emitido.

print("------------------------------")
velocidade_ventos = int(input("Qual a velocidade do vento (Km/h): "))
print("------------------------------")
quantidade_chuva  = int(input("Qual a quantidade de chuva (mm) "))
print("------------------------------")

if velocidade_ventos> 60 and quantidade_chuva > 50:
    print("Alerta de tempestade")
elif velocidade_ventos > 60 or quantidade_chuva > 50:
    print("Alerta")
else:
    print("Sem nenhum alerta")
print("------------------------------")

#DEU CERTO DE PRIMEIRA KKKKKKKKKK 