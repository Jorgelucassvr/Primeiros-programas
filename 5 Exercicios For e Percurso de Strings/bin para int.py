p = int(input("insira seu numero: "))
linha =""
for i in range (1, p+1):
    linha += str(i) 
    print (linha)
for i in range (len(linha)-1,-1,-1):
    contador=""
    for j in range (1 , p ):
        contador += str(j) 
    p-=1
    print (contador)