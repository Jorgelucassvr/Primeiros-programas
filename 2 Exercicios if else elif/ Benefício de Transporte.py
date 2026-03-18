# concede gratuidade para passageiros que tenham 65 anos ou mais 

#ou que possuam deficiência registrada no sistema.

#Se pelo menos uma dessas condições for verdadeira, 

# o sistema deve indicar que o passageiro tem direito à gratuidade.

# Else, o sistema deve indicar que o passageiro não possui esse benefício.

print("------------------------------------- \nSistema de Benifecios para trasporte")
Idade = int(input("Informe a Idade: "))
print("-------------------------------------")
Deficiencia = str(input("Possue alguma deficiencia(sim/nao)"))
if Idade <= 0:
    print ("-------------------------------------\nErro\n-------------------------------------")

elif Idade >= 65 or Deficiencia.lower() == "sim":
    print("-------------------------------------\nVoce tem acesso ao beneficio\n-------------------------------------")
else:
   print("-------------------------------------\nVoce nao acesso ao beneficio\n-------------------------------------")