treino = []
pico = 0
picos = []
picos_posicoes = []
for _ in range (10):
    p = float(input("insira os treinos: "))
    treino.append(p)
for p in range (10):
    anterior = treino[p-1]
    atual = treino[p]
    if p != 9 :
        proxima = treino[p+1]
    print (proxima)
    if atual > proxima and atual >anterior:
        pico+=1
        picos_posicoes.append(p)
        picos.append(atual)
print ("Quantidade de picos: ",pico)
print ("Posiçoes dos picos: ", picos_posicoes)
print ("Valores dos picos: ",picos)