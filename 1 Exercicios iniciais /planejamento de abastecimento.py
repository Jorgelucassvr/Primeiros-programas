#distancia media percorrida em cada entrega (em Km)
#número médio de entregas realizadas por dia
#número de dias de trabalho na semana
#consumo médio do veículo em quilômetros por litro (km/l)
#preço do combustível em reais por litro

#a partir dessas informações, o programa deve calcular:

#a distância total percorrida por dia
#a distância total percorrida na semana
#a quantidade de combustível necessária na semana
#o custo total estimado de combustível na semana

#Entrada
distancia = int(input("Distancia media percorrida no dia: "))
entregas_feitas_dia = float(input("Numero de entregas feitas no dia: "))
dias_trabalhados = int(input("Dias trabalhados na semana: "))
consumo_medio_veiculos = float(input("Qual consumo medio dos veiculos por lintro: "))
preço_do_combustivel = float(input("Preço do combustivel, reais por lintro: "))
#Calculo
distancia_total_dia = distancia * entregas_feitas_dia
distancia_total_semana = distancia_total_dia * dias_trabalhados
combustivel_necessario_semana = distancia_total_semana / consumo_medio_veiculos
custo_total_combustivel_por_semana = preço_do_combustivel * combustivel_necessario_semana
#Saida
print("Relatorio de operaçao do veiculo")
print("--------------------------------")
print(f"Distancia diaria: {distancia_total_dia:.0f}Km")
print(f"Distancia semanal:{distancia_total_semana:.0f}Km")
print(f"combustivel necessario: {combustivel_necessario_semana:.2f}Litros ")
print(f"Custo semanal de combustivel: {custo_total_combustivel_por_semana}R$")