Rep,armazenamento,Atual =0,0,0
n = int(input("insira um numero:"))
while n != 0:
    if n> Atual:
        Rep+=1
        armazenamento = Rep
    atual = n
    n = int(input("insira um numero:"))
print ( armazenamento)