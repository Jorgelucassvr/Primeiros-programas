def multiplicar(a,b):
    if  b == 0 :
         return 0
    if a > 0 and b < 0 :
         if a == 0:
              return 0 
         return b + multiplicar(b,a-1)
    if a and b <= 0:
         if a == 0:
              return 0
         return -a + multiplicar(a,b+1)
    
    return a + multiplicar(a,b-1)
    
print(multiplicar(8 ,0))