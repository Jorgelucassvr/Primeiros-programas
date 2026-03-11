#Relatório de consumo
#Consumo diário (kWh): 
#Consumo mensal (kWh): 
#Custo mensal (R$): 
#Para calcular o consumo diário, 
# devemos calcular: (potencia * horas) / 1000
potencia = int(input("Digite a potência do aparelho em watts (W): "))
horas = int(input("Digite o número de horas que o aparelho é utilizado por dia: "))
consumo_diario = (potencia * horas) / 1000
print(f"Consumo diário: {consumo_diario:.2f} kWh")
consumo_mensal = consumo_diario * 30
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
custo_mensal = consumo_mensal * 0.50
print(f"Custo mensal: R${custo_mensal:.2f}")