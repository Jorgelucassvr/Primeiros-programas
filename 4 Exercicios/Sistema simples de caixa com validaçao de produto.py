

###### menu de opçoes #######
#1 Registro de venda
#2 Mostrar total vendido
#3 Mostrar quantidade de vendas
#4 Mostrar ticket medio das vendas 
#5 Mostrar qauntidade vendida por tipo de produto 
#0 encerrar 

##l
#1 Lanche 
#2 bebida 
#3 Sobremesa

# - mesagem de erro 
# - valor invalido 
lanche = 0
bebida = 0
sobremesa = 0
venda = 1
numero = 1 
tt1 = ("(AINDA NAO HOUVE VENDAS)") 
t1 = ("(AINDA NAO HOUVE VENDAS)")
l1 = ("")
b1= ("")
s1 = ("")
venda_passou = 0 
venda_1 = 0
ticket_medio = 0
total_vendas =0

while numero != 0:
     if bebida + lanche + sobremesa >= 1:
      tt1 = ""
     print("-------------------------------------------------\n Menu inicial")
     numero = int(input(f"\n1: Registrar Venda \n\n2: Total de intens vendidos            {tt1}\n\n3: Quantidade de vendas por Cantegoria {tt1} \n\n4: Ticket medio das vendas             {tt1}\n\n0: Sair \n\n>>>>>Insira o digito desejado: "))
     venda = venda + 1  
#primeiro termo 
     if numero == 1 :
        while venda != 0:
             print("Menu de vendas:")
             venda = int(input("\n1: Lanche 5R$ \n\n2: Bebida 2R$\n\n3: Sobremesa 5R$\n\n0: Sair\n\n>>>>>Insira o digito desejado: "))
             if venda == 1:
                 lanche = lanche + 1 
                 venda_passou = venda_passou + 1
             elif venda == 2:
                 bebida = bebida + 1
                 venda_passou = venda_passou + 1
             elif venda == 3:
                 sobremesa = sobremesa+ 1 
                 venda_passou = venda_passou + 1
             elif venda == 0:
                 venda == 0
             else:
                 venda == 1
                 print("-------------------------------------------------")
                 print("ALERTA DE ERRO:")
                 print("valor digitado incorretamente, Tente novamente:")
                 print("-------------------------------------------------")          
             if venda_passou > 0:
                venda_1 = venda_1 + 1 
             venda_passou = venda_passou = 0
#calculo-----------------------------------
        total = lanche + bebida + sobremesa
        lanche_v = lanche * 5 
        bebida_v = bebida * 2
        sobremesa_v = sobremesa * 5
        total_vendas = lanche_v + bebida_v + sobremesa_v
        ticket_medio = total_vendas / venda_1
        if lanche  == 0:
         l1 = ("(AINDA NAO HOUVE VENDAS)")
        if lanche <0:
         l1 = ("")
        if bebida  == 0:
         b1 = ("(AINDA NAO HOUVE VENDAS)")
        if bebida <0:
         b1 = ("")  
        if sobremesa  == 0:
         s1 = ("(AINDA NAO HOUVE VENDAS)") 
        if sobremesa < 0:
         s1 = ("")
        if lanche + bebida + sobremesa == 0 :
         t1 = ("(AINDA NAO HOUVE VENDAS)")   
        if total_vendas + total < 0:
         t1 = ("")
#segundo termo                    
     if numero == 2:
        while venda !=0:
             print ("\n\n")
             print("-------------------------------------------------\n")
             venda = int(input(f">>> Total de vendas em R$: {total_vendas} <<<\n\n1: Calcular novamente\n\n0: Sair\n\n>>>>>Insira o digito desejado: "))
             if venda == 1:
                 venda = 1 
             elif venda == 0:
                 venda = 0
             else:
                 venda = 1
                 print("-------------------------------------------------")
                 print("ALERTA DE ERRO:")
                 print("valor digitado incorretamente, Tente novamente:")
#terceiro termo
     if numero == 3:
        while venda !=0:                      
             print("-------------------------------------------------")
             print("\nQuantidade vendida por categoria:")                         
             venda = int(input(f"\n1: Total de produtos vendidos    {tt1}\n\n2: Total de lanches vendidos     {l1}\n\n3: Total de bebidas vendidas     {b1}\n\n4: Total de sobremesas vendidas  {s1} \n\n5: Total geral                   {tt1}\n\n0: Sair\n\n>>>>>Insira o digito desejado: "))
             if venda == 1:
                 while venda != 0:
                  print("-------------------------------------------------")
                  print(f"Total de produtos vendidos: {total} ")
                  print("-------------------------------------------------")
                  venda= int(input("\n0: Sair\n\n>>>>>Insira o digito desejado:"))                  
                 if venda == 0:
                   venda == 0
                 else:
                   venda == 1
                 print("-------------------------------------------------")
                 print("ALERTA DE ERRO:")
                 print("valor digitado incorretamente, Tente novamente:")
                 print("-------------------------------------------------")
             elif venda == 0:
                 venda ==0
             elif venda == 2:
                   while venda != 0:
                     print("-------------------------------------------------")
                     print(f" Total de lanches vendidos: {lanche} ")
                     print("-------------------------------------------------")
                     venda = int(input("\n\n0: Sair\n\n>>>>>Insira o digito desejado:"))
                     if venda == 0:
                      venda == 0
                     else:
                      venda == 1
                     print("-------------------------------------------------")
                     print("ALERTA DE ERRO:")
                     print("valor digitado incorretamente, Tente novamente:")
                     print("-------------------------------------------------")

                     
             elif venda == 3:
                   while venda != 0:
                     print("-------------------------------------------------")
                     print(f"Total de bebidas: {bebida} ")
                     print("-------------------------------------------------")
                     venda = int(input("\n\n0: Sair\n\n>>>>>Insira o digito desejado:"))
                     if venda == 0:
                      venda == 0
                     else:
                      venda == 1
                     print("-------------------------------------------------")
                     print("ALERTA DE ERRO:")
                     print("valor digitado incorretamente, Tente novamente:")
                     print("-------------------------------------------------")
             elif venda == 4:
                   while venda != 0:
                     print("-------------------------------------------------")
                     print(f"Total de sobremesas: {sobremesa} ")
                     print("-------------------------------------------------")
                     venda = int(input("\n\n0: Sair\n\n>>>>>Insira o digito desejado:"))
                     if venda == 0:
                      venda == 0
                     else:
                      venda == 1
                     print("-------------------------------------------------")
                     print("ALERTA DE ERRO:")
                     print("valor digitado incorretamente, Tente novamente:")
                     print("-------------------------------------------------")
             elif venda == 5:
                   while venda != 0:
                     print("--------------------------------------------------------------------------------------------------------")
                     print(f"Total de lanches: {lanche}\nTotal de bebidas: {bebida}\nTotal de sobremesas{sobremesa}\ntotal: {total}")
                     print("--------------------------------------------------------------------------------------------------------")
                     venda = int(input("\n\n0: Sair\n\n>>>>>Insira o digito desejado:"))
                     if venda == 0:
                      venda == 0
                     else:
                      venda == 1
                     print("-------------------------------------------------")
                     print("ALERTA DE ERRO:")
                     print("valor digitado incorretamente, Tente novamente:")
                     print("-------------------------------------------------")    
             else:
                 venda == 1
                 print("-------------------------------------------------")
                 print("ALERTA DE ERRO:")
                 print("valor digitado incorretamente, Tente novamente:")
     if numero == 4:
         while venda != 0:
          print("-------------------------------------------------")
          print(f"\nTicket medio das vendas:{ticket_medio}") 
          venda = int(input("0: Sair "))
         if venda == 0:
            venda =0
         else:
             venda == 1
             print("-------------------------------------------------")
             print("ALERTA DE ERRO:")
             print("valor digitado incorretamente, Tente novamente:")
     if numero == 0:
        numero ==0
        print("--------------------------------------------------------------------------------------------------------")
        print("Aqui esta o total:")
        print(f"Total de lanches: {lanche}\nTotal de bebidas: {bebida}\nTotal de sobremesas{sobremesa}\ntotal: {total}")
        print("--------------------------------------------------------------------------------------------------------")