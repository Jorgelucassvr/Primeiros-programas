#matricula;nome;nota1;nota2;nota3
lista = {}

with open("/Users/jorgelucasvieira/Documents/Introdrucao a algoritmos/10/arquivo.txt","r") as arquivo:
    for elementos in arquivo:
        matricula , nome , nota1 , nota2 , nota3 = elementos.split(";")
        lista[matricula] = {
            "nome": str(nome),
            "nota1": float(nota1),
            "nota2": float(nota2),
            "nota3": float(nota3),
        }
with open("resultado.txt","x")as arquivo:
    for matricula in lista:
        nome = lista[matricula]["nome"]
        nota1 = lista[matricula]["nota1"]
        nota2 = lista[matricula]["nota2"]
        nota3 = lista[matricula]["nota3"]
        total = nota1+nota2+nota3
        media = total/3
        if media >= 70:
            situacao = "Aprovado"
        elif media >= 40:
            situacao = "Podera fazer exame especial"
        else:
            situacao = "Reprovado"
        arquivo.write(
            f"O aluno com matricula: {matricula} "
            f"Nome: {nome} "
            f"Com media: {media:.2f} "
            f"Situacao: {situacao}\n"
        )



