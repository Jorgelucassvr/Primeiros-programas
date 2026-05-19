numeros = [] 
sem_duplicatas= []

for _ in range (1, 21):
     numero = int(input(f"insira o numero {_}: "))
     numeros.append(numero)
     
print (numeros)

def eliminar_duplicatas(numeros):
     for numero in numeros:
        if numero not in sem_duplicatas :
            sem_duplicatas.append(numero)
    
     print(sem_duplicatas)
     return sem_duplicatas

eliminar_duplicatas(numeros)

