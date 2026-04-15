Idade = int(input("insira sua idade:"))
matricula = input("matricula ativa ? (sim/nao) ")
autorizaçao =input("possue autorizaçao? (sim/nao) ")

if Idade>= 18 and matricula.lower() == "sim":
    print ("acesso permitido")
elif autorizaçao.lower() == "sim":
    print ("acesso permitido")
else:
    print("acesso negado")