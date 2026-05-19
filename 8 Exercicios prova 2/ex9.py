armazenamento = float(input("insira a capacidade: "))

def processar_pedidos(pedido):
    while pedido <= armazenamento:
        if pedido > armazenamento:
            print ("nao foi possivel fazer o pedido")
        elif pedido <= armazenamento:
            armazenamento-=pedido
            print (f"o pedido foi feito resta: Kg{armazenamento}")
        pedido = float(input("insira o pedido: "))
    print ("nao foi possivel fazer o pedido")