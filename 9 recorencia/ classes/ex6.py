def contar_digitos(numero):
    if numero == 10:
            return 1
    return  1 + contar_digitos( numero // 10 )
res = contar_digitos(9)
print(res)