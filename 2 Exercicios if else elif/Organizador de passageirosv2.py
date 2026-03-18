#1 grupo: prioritário
#2 grupo: executivo
#3 grupo: ouro economico   
#4 grupo: prata economico
#5 grupo: comum economico e atrasados
print("Possue alguma deficiencia?")
resposta_prioridade = str(input("(sim/nao) " ))
if resposta_prioridade.lower() == ("sim"):
    print ("voce tem prioridade 1!")
elif resposta_prioridade.lower() == ("nao"):
    print("Chegou atrasado?")
    resposta_prioridade = str(input("(sim/nao) " ))
    if resposta_prioridade.lower() == ("sim"):
        print("voce tem prioridade 5!")
    elif resposta_prioridade.lower() == ("nao"):
        print("Qual seu nivel de prioridade:")
        resposta_prioridade = str(input("Executivo ou Economico? " )) 
        
        if resposta_prioridade.lower() == ("executivo"):
         print("Voce tem prioridade 2!")
        elif resposta_prioridade.lower()==("economico"):
            print("Qual a sua classe?")
            resposta_prioridade = str(input("Ouro - Prata - Comum " )) 

            if resposta_prioridade.lower() == ("ouro"):
                 print("Voce tem prioridade 3!")
            elif resposta_prioridade.lower() == ("prata"):
                 print("Voce tem prioridade 4!")
            elif resposta_prioridade.lower() ==("comum"):
                print("Voce tem prioridade 5!")
            else:
                 print("Resposta invalida")
        else:
            print("Resposta invalida")
    else:    
        print("Resposta invalida")
else:
    print("Resposta invalida")