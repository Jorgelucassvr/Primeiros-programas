id_= 1
dia_ = -1
dia_validaçao = "par"
id_validaçao = "par"
while id_ > 0 :
    while dia_ < 0:
        dia_ = int(input("Qual dia do mes (1 a 30): "))
        if dia_ > 30:
            dia_ = -1
    id_ = -1
    while id_ < 0 :
        id_ = int(input("qual seu id (1 a 7): "))
        if id_ > 7:
            id_ = -1
    if dia_  % 2 != 0:
        dia_validaçao  = "impar"
    if id_ % 2 != 0:
        id_validaçao = "impar"
    if dia_validaçao.lower() != id_validaçao.lower():
        print ("Nao sera possivel fazer plantao neste dia ")
    else:
        print ("Vai ser possivel fazer plantao neste dia  ")
    dia_validaçao = "par"
    id_validaçao = "par"