nota=float(input("qual a nota do aluno? "))


if nota<=100 and nota>=90:
    print("nota exelente")
elif nota<=89 and nota >=70:
    print("nota Boa")
elif nota <= 69 and nota >= 50:
    print("nota Regular")
else:
    print("nota insuficiente")