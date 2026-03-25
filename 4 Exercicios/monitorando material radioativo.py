

peso = int(input("peso atual do material: "))
peso_inicial = peso
tempo = 1
while peso >= 0.25:
 tempo = tempo + 50
 peso = peso / 2

tempo = tempo / 60
 

 

print(f"Massa inicial {peso_inicial}\nTempo que passou (em min) {tempo:.2f}\nMassa do material (em gramas) {peso:.2f}")