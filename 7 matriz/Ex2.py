list = []
total = 0
for _ in range (6):
    n = float(input("insira as notas: "))
    list.append(n)
for n in list:
    total+= n 
media = total/ len(list)
print("total",total)
print("media",media)