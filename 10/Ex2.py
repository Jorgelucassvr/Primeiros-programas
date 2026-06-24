
lista_nomes = []
nomes_lidos_1 = 0
nomes_lidos_2 = 0
nomes_lidos_total = 0
with open("/Users/jorgelucasvieira/Documents/Introdrucao a algoritmos/10/nome1.txt","r")as nome1:
    for nome in nome1:
        nome = nome.strip("\n")
        nomes_lidos_1 += 1
        if nome not in lista_nomes:
            nomes_lidos_total += 1
            lista_nomes.append(nome)
with open("/Users/jorgelucasvieira/Documents/Introdrucao a algoritmos/10/nome2.txt","r") as nome2:
    for nome in nome2:
        nome = nome.strip("\n")
        nomes_lidos_2+=1
        if nome not in lista_nomes:
            nomes_lidos_total+=1
            lista_nomes.append(nome)
with open("nomes_mesclados.txt","x") as arquivo:
    for nome in lista_nomes:
        arquivo.write(nome + "\n")

    arquivo.write(f"nomes lidos no primeiro arquivo = {nomes_lidos_1}\n")
    arquivo.write(f"nomes lidos no segundo arquivo = {nomes_lidos_2}\n")
    arquivo.write(f"nomes distintos lidos = {nomes_lidos_total}\n")