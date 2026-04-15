valido = 1
letra = 0
numero = 0
contador =1
while valido != 0:
    senha = str(input("insira a senha: "))
    for i in (senha):
        contador+=1
        if  i in "1234567890":
            numero = 1
        print("numero",numero)
        if i.lower() in "abcdefghijklmnopqrstuvwxyz":
            letra = 1
        print("letra",letra)
        print(contador)
        if contador > 8 and letra > 0 and numero > 0:
            valido = 0
print ("senha valida ")
