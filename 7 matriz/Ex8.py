nomes = []
encontrado = False
visto= 0
for _ in range (8):
    nome= input("insira o nome: ")
    nomes.append(nome)
nome = input("insira o nome a ser procurado:")
for nomes_listados in nomes:
    if nome.lower() == nomes_listados.lower():
        encontrado = True
        visto += 1
if encontrado :
    print (f"nome foi encontrado.\nQuantidade de vezes: {visto}")
else:
    print("nome nao foi encontrado")