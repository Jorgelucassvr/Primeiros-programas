



opcoes = 1
n1 = 1
total = 0
total_lucro =0
aporte_total= 0
saldo_medio=0
while opcoes != 0: 
    opcoes = int(input("1 - Configurar simulaçao\n2 - Executar simulaçao\n3 - Mostrar relatorio geral\n0 - Encerrar sistema\n>>>>>> "))
    if opcoes == 1:
        print ("\n\n\nMenu de configuraçao")
        investido = int (input("insira o investimento inicial: "))
        aporte = int (input ("aporte mensal: "))
        x = int(input("insira o juros mensal(%): "))
        tempo = int (input("quantidade de messes: "))
        total = investido
        juros = (x/100)+1
    if opcoes == 2:
        for i in range (1, tempo+1):
            total+= aporte 
            total*= juros
            aporte_total+= aporte
        total_lucro = total - (aporte_total +investido)
        saldo_medio = total / tempo
    if opcoes == 3:
        print("investimento:", investido)
        print("aporte:", aporte)
        print("taxa de juros %:",x)
        print("total de meses:", tempo)
        print("saldo final:", total)
        print("total lucro:",total_lucro)
        print("saldo medio:",saldo_medio)