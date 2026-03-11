nome = str(input("insira o nome do funcionario: ")) 
salario = float(input("Qual o salario base do funcionario? R$"))    
if salario <= 0:
    print("o salario deve ser maior que R$0,00") 
    import sys
    sys.exit(0)
bonus = float(input("Qual a porcentagem de bônus do funcionario? "))   
if bonus <= 0:
     print("o bonus deve ser maior que 0%") 
     sys.exit(0)
if bonus > 100:
    print("o bonus deve ser menor ou igual a 100%") 
    sys.exit(0)
bonus_total = salario + (salario * (bonus / 100))
print(f"O bonus aplicado foi de = R${bonus_total - salario:.2f}")
print(f"O salario total do funcionario {nome} e de = R${bonus_total:.2f}")