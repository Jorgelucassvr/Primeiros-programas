
n = 1
ultimo = 0
quanto = 1
mensagem = "nao existe padrao"
while n != 0:
    n = int(input("insira o numero: "))
    if n == ultimo:
        quanto += 1
    if ultimo != n:
        quanto = 1
    if quanto == 3:
        mensagem = "existe padrao"
    print("ultimo",ultimo)
    print("quanto",quanto)
    ultimo = n
print(mensagem)