#preço do produto
#percentual do imposto (valor de 0 a 100%)
#valor do frete 
#alor de imposto cobrado\
#valor total(preço somado ao imposto e frete)\
preço_do_produto = float(input("Digite o precço do produto em Reais:"))
imposto = float(input("Digite valor do imposto em porcentagem:"))
frete = float(input("Digite o valor do frete: "))

percentual_de_imposto = imposto / 100
imposto_aplicado = preço_do_produto * percentual_de_imposto

valor_total = imposto_aplicado + preço_do_produto + frete
print(f"Valor do imposto {imposto_aplicado:.2f} \n Valor total: {valor_total:.2f} R$")