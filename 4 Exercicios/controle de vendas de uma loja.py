valor_total = 0
quantidade_vendas = 0
valor_medio = 0
parar_sistema = 1
while parar_sistema >= 0:
     venda = int(input("Valor da venda em R$: "))
     if venda == 0:
        parar_sistema = -1
     else:
         valor_total = valor_total + venda
         quantidade_vendas= quantidade_vendas+ 1 
valor_medio = valor_total / quantidade_vendas
print(f"Valor total de vendas: {valor_total}\nQauntidade de vendas: {quantidade_vendas}\nTicket medio: {valor_medio}")