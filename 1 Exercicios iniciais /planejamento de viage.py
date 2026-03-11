#distancia da viagem (km)
#cosumo do carro (km/l)
#preço do litro da gasolina (R$ litro)
distancia_viagem = float(input("Digite a distância da viagem em km: "))
consumo_carro = float(input("Digite quantos km o carro faz por litro: "))
preco_gasolina = float(input("Digite o preço do litro da gasolina em R$: "))
litros_necessarios = distancia_viagem / consumo_carro
consumo_estimado = litros_necessarios * preco_gasolina
print(f" PLANRJAMENTO DA VIAGEM \nGasolina necessaria: {litros_necessarios:.2f} Litros \nCusto necessario:{consumo_estimado:2.2f}R$")