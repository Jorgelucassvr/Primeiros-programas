idade= int(input("Qual a sua idade? "))
valor_da_compra= float(input("Qual valor da compra? "))
if idade <=0 or valor_da_compra<0:
    print("valores invalidos")
elif idade >= 60 or valor_da_compra> 200:
    print("cliente elegivel para desconto")
else:
    print("Cliente sem desconto ")