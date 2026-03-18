idade = int(input("qual a idade do estudande? "))
Matricula_evento = str(input("o estudante esta matriculado no evento (sim/nao) ? "))

if Matricula_evento.lower() == "sim" and idade >= 18:
 print("Acesso permitido")
else:
 print ("Acesso negado")
