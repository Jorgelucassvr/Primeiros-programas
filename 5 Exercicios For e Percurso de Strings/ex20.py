nome =""
armazenado = 0
calculo = 0
qunt_critica =0
qunt_abaixo =0
qunt_adequado =0
while nome.lower() != "fim":
    quantia_atual = 0
    quantia_minima = 0
    nome = str(input("nome do produto: "))
    if nome.lower() == "fim":
        print ("Acabou")
    else:
         while quantia_atual == 0:
             quantia_atual = int (input("quantidade atual: "))
             quantia_minima = int(input("quantia minima: "))
             if quantia_atual < 0 or quantia_minima < 0:
                 quantia_atual = 0
                 quantia_minima = 0
                 print ("valor incorreto")
 #calculo
    critica = "estoque critico"
    abaixo = "estoque abaixo"
    adquado = "estoque adquado"
    situaçao = ""
 #condicionais 
    if nome.lower() == "fim":
        print ("")
    else:
         if quantia_atual  < (quantia_minima * 0.5):
          situaçao = critica
          qunt_critica+= 1 
         elif quantia_atual < quantia_minima:
          situaçao = abaixo
          qunt_abaixo+=1
         else:
          situaçao = adquado
         qunt_adequado+= 1
    
         calculo = quantia_atual - quantia_minima
         if calculo > armazenado:
            armazenado = calculo
         print (f"A situaçao do produto {nome} é {situaçao}")
#saidas
if qunt_adequado == 0 and qunt_abaixo == 0 and quantia_atual == 0:
    print ("Dados invalidos")
else:
    print (f"quantos ficaram\ncriticos = {qunt_critica}\nabaixo = {qunt_abaixo}\nadquando = {qunt_adequado}")

    