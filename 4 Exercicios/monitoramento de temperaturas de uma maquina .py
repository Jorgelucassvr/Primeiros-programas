quantas_temperaturas = 0
maior_temperatura = 0 
menor_temperatura = 0
media_temperatura = 0
quantas_acima_de_80 = 0
soma_temperatura = 0
fim = 1
while fim >= 0:
    temperatura_atual = int(input("informe a temperatura atual: "))
    if temperatura_atual > 0:
     quantas_temperaturas = quantas_temperaturas + 1
    if temperatura_atual > 80:
     quantas_acima_de_80 = quantas_acima_de_80 + 1
    if temperatura_atual == -1:
     fim = -1 
    elif temperatura_atual > maior_temperatura:
     maior_temperatura = temperatura_atual
    elif temperatura_atual < menor_temperatura or menor_temperatura == 0:
     menor_temperatura = temperatura_atual 
    soma_temperatura = temperatura_atual + soma_temperatura
media_temperatura = soma_temperatura / quantas_temperaturas 
print(f"Temperaturas registradas: {quantas_temperaturas}\nMaior temperatura: {maior_temperatura}\nMenor temperatura: {menor_temperatura}\nmedia das temperaturas: {media_temperatura}\nacima de 80 graus: {quantas_acima_de_80}")