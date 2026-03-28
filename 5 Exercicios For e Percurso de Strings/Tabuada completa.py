n_limite= int(input("até qual numero voce quer sua tabuada: ")) 
for  contador in range(1, n_limite + 1 ):
    for repetçoes in range(1,11):
        resultado = contador* repetçoes 
        print (f"Tabuada do {contador}\n\n {contador} x {repetçoes} = {resultado}\n")
    print("------------------")