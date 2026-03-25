tabuada = 1
numero = 1
while numero <= 10:
   while tabuada < 11:
        resultado = numero * tabuada
        print(f"Tabuada do {numero}\n {numero} x {tabuada} = {resultado}")
        tabuada = tabuada + 1 
   numero = numero + 1 
   if tabuada == 11:
       tabuada = tabuada - 9
   
    
