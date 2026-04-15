



estoque = float(input("Capacidade do silo (kg): "))

total_distribuido = 0
contador = 0

while estoque > 0:
    pedido = float(input("Quantidade desejada (kg): "))
    if pedido > estoque:
        print("Pedido não pode ser atendido por falta de estoque.")
    estoque -= pedido
    if pedido < estoque:
        total_distribuido += pedido
        contador -=1
    contador += 1

print("\nResumo do dia:")
print("Total distribuído:", total_distribuido, "kg")
print("Agricultores atendidos:", contador)