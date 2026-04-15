
n = 1
n_1 = 0
quantos = 0
ultima_vez = 0
while n != 0:
    n = int(input("insira um numero: "))
    if n > n_1:
        quantos+= 1
        n_1 = n
    elif n < n_1:
        quantos = 1
        n_1 = -1
    if ultima_vez < quantos:
        ultima_vez  = quantos 
print(ultima_vez)