#deve classificar o índice UV em quatro categorias de risco:

#baixo, moderado, alto ou muito alto, de acordo com o valor do índice informado. 

#aplicativo poderá exibir ao usuário uma indicação clara do nível de exposição ao qual ele está sujeito.

Indice_uv = float(input("\n\nCALCULE O RISCO DE EXPOSIÇAO AOS RAIOS ULTRA VIOLETAS: \n Qual o nivel de rediaçao atual? "))
if Indice_uv >= 10:
     indice_final = ("Risco de morte eminente")
elif Indice_uv >=7.5:
     indice_final = ("Risco muito alto")     
elif Indice_uv >=5:
     indice_final = ("Risco alto")
elif Indice_uv >=2.5:
     indice_final = ("Risco moderado")
elif Indice_uv >=0:
     indice_final = ("Risco Baixo")
else:
    indice_final = ("Invalido")

print(f".\n.\n.\n-------------------------------\n Nivel da radiaçao UV apresenta:\n          {indice_final} \n-------------------------------\n.\n.\n.")