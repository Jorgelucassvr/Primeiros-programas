import viagem_funçoes as v
#input
valor_passagem = float(input("insira o valor da passagem: "))
valor_bagagem= float(input("insira o valor da passagem(opcional): "))
valor_diaria = float(input("insira o valor da diaria: "))
quantidade_de_dias= float(input("insira a quantidade de dias: "))
taxa_extra = float(input("insira a taxa extra (opcional): "))
total_horas = float(input("insira o total de horas: "))
alimentacao = float(input("insira o total gasto com alimentacao (opcional): "))
#calculo
valor_final_passagem = v.calcular_passagem(valor_passagem, valor_bagagem)
valor_final_hospedagem = v.calcular_hospedagem(valor_diaria,quantidade_de_dias,taxa_extra)
duraçao_dias,duracao_horas = v.converter_duracao(total_horas)
#print 
print (f"valor da passagem: R${valor_passagem}")
print (f"valor hospedagem: R${valor_final_hospedagem}")
print (f"Duraçao da viagem Dias:{duraçao_dias} Horas:{duracao_horas}")
print(f"Custo fixo: R${(valor_passagem + valor_final_hospedagem) - taxa_extra}")
print (f"Custo extra: R${taxa_extra+valor_bagagem+alimentacao}")
print (f"Custo total : R${valor_final_hospedagem+valor_final_passagem}")