#total de paginas do livro 
#numero medio de palavras por pagina 
#a velocidade media de leitura em palavras por minuto 
#quantidade de minutos disponiveis para leitura no dia 

#Planejamento de leitura
# -----------------------
#Total de palavras no livro: 
#Tempo total de leitura (minutos): 
#Tempo total de leitura (horas): 
#Dias estimados para terminar o livro: 
#Entrada 
total_de_paginas = int(input("Total de paginas do livro: "))
media_palavras_por_paginas = float(input("Media de palavras por pagina: "))
palavras_por_min = float(input("Quantas palavras sao lidas (por min): "))
minutos_disponiveis = float(input("Quantos minutos sao disponiveis para leitura (por dia) ? "))
#Calculo
total_de_palvras_livro = total_de_paginas * media_palavras_por_paginas
tempo_total_leitura_em_min = (media_palavras_por_paginas * total_de_paginas) / palavras_por_min
tempo_total_leitura_em_horas = tempo_total_leitura_em_min / 60
dias_estimados_para_terminar_o_livro = tempo_total_leitura_em_horas/ 24
#Saida
print("planejamento de leitura")
print("-----------------------")
print(f"Total de palavras no livro: {total_de_palvras_livro: .0f}Palavras")
print(f"Tempo total de leitura: {tempo_total_leitura_em_min: .1f}Minutos")
print(f"Tempo total de leitura: {tempo_total_leitura_em_horas:.1f}Horas")
print(f"Dias ate acabar o livro:  cerca de {dias_estimados_para_terminar_o_livro:.0f} Dias")
