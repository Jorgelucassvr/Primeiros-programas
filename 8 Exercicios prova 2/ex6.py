n = int(input("Quantas matrículas: "))

algoritmos = set()
calculo = set()

for _ in range(n):
    matricula = input("Matrícula Algoritmos: ")
    algoritmos.add(matricula)

for _ in range(n):
    matricula = input("Matrícula Cálculo: ")
    calculo.add(matricula)

ambas = algoritmos & calculo
apenas_uma = algoritmos ^ calculo

print(f"Matriculados em ambas: {ambas}")
print(f"Matriculados em apenas uma: {apenas_uma}")