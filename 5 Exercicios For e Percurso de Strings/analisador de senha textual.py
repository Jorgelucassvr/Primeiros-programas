senha = (input("digite a senha "))
maiusculo = 0
minusculo = 0
numero = 0
total = 0
especiais = 0
for i in senha:
    total+= 1
    if i in ("QAZWSXEDCRFVTGBYHNUJMIKLPCÇ"):
        maiusculo+= 1
    if i in ("1234567890"):
        numero +=1
    if i in ("qazwsxedcrfvtgbyhnujmikolp;"):
        minusculo+= 1
    if i in ("!@#$%ˆ&*_-+=.,<>?/"):
        especiais+= 1
if total >= 8 and minusculo >= 1 and maiusculo >= 1 and numero >= 1 and especiais >= 1:
    print ("senha forte---")
else:
    print ("senha fraca---")
print ("especiais ",especiais )
print ("numeros",numero)
print ("maiusculo",maiusculo)
print ("minusculo",minusculo)
print ("especial",  especiais)
print ("total",total)
