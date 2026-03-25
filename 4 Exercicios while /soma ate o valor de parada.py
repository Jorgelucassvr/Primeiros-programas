numeros_digitados = 0
numeros_soma = 0
contagem = 1 
contagem_numero = 0
while contagem >= 0:
    numero = int(input("Digite os numeros que voce deseja somar \n(digite 0 para parar): "))
    if numero == 0:
        contagem = contagem = -1
    else:
        numeros_soma = numeros_soma + numero 
        contagem_numero = contagem_numero + 1 
print(f"A soma foi = {numeros_soma}\nForam somados {contagem_numero} numeros")

