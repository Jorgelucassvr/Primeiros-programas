def calcular_passagem(valor_base, bagagem=0):
    total = valor_base + bagagem
    return total
def calcular_hospedagem(valor_diaria, dias=1, taxa_extra=0):
    total = (valor_diaria * dias) +taxa_extra
    return total
def converter_duracao(total_horas):
    total_dias = total_horas//24
    total_h = total_horas % 24
    return total_dias,total_h
def calcular_orcamento(passagem_total, hospedagem_total, alimentacao=0):
    total = passagem_total + hospedagem_total +alimentacao
    return total
    ghjhhuuhuiyuuiuiyiuhoij