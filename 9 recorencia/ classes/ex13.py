def eh_primo(numero, divisor):
    if numero < 2:
        return False
    if divisor * divisor > numero:
        return True
    if numero % divisor == 0:
        return False
    return eh_primo(numero, divisor + 1)


inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio > fim:
    inicio, fim = fim, inicio

quantidade = 0

for numero in range(inicio, fim + 1):
    if eh_primo(numero, 2):
        print(numero)
        quantidade += 1

print("Quantidade total de primos:", quantidade)