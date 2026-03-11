Nome = str(input("insira o nome do passageiro: ")) 
atendimento = str(input(" atendimento prioritário? (sim ou não) "))
if atendimento == "sim": 
    print("o passageiro", Nome, "tem direito a atendimento prioritário *primeiro grupo*")    
    grupo=1
    import sys 
    sys.exit(1)
atendimento = str(input("voce chegou atrasado? (sim ou não) "))
if atendimento == "sim":    
    grupo=6
    print("o passageiro", Nome, "tem direito a atendimento de *Quinto grupo*") 
    sys.exit(2)
atendimento = str(input("atendimento executivo? (sim ou não) "))
if atendimento == "sim":    
    grupo=2
    print("o passageiro", Nome, "tem direito a atendimento executivo de *Segundo grupo*") 
    sys.exit(3)   
atendimento = str(input(" comum, prata ou ouro? ")) 
if atendimento == "ouro":
    print("o passageiro", Nome, "tem direito a atendimento ouro de *Terceiro grupo*")
if atendimento == "prata":
    print("o passageiro", Nome, "tem direito a atendimento prata de *Quarto grupo*")
if atendimento == "comum":
    print("o passageiro", Nome, "tem direito a atendimento comum de *Quinto grupo*")
#1 grupo: prioritário
#2 grupo: executivo
#3 grupo: ouro economico   
#4 grupo: prata economico
#5 grupo: comum economico e atrasados 