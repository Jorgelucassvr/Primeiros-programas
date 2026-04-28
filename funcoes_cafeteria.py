def calcular_preco_cafe(preco_base,acresimo=0):
    preço_cafe = preco_base + acresimo
    return preço_cafe
def calcular_acompanhamento(preco,desconto=0):
    desconto = (desconto / 100) + 1 
    preco_acompanhamento = preco * desconto
    return preco_acompanhamento
def resumo_item(nome, valor):
    print (f"{nome} tem o valor final de R${valor}")
def calcular_totais(valor1,valor2,taxa_servico=10):
    taxa_servico = (taxa_servico/100) +1
    valor1 = valor1 * taxa_servico
    valor2 = valor2 * taxa_servico
    return valor1, valor2
