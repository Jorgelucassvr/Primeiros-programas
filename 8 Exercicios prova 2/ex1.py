senhas = ["Senhas validas"]
def validar_senha(senha):
    if len(senha) < 8:
        return
    if " " in senha:
        return

    tem_numero = False
    tem_letra = False

    for digito in senha:
        if digito in "1234567890":
            tem_numero = True
        if digito in "abcdefghijklmnopqrstuvwxyz":
            tem_letra = True

    if tem_numero and tem_letra:
        senhas.append(senha)

senha = ""
while senha.lower() != "sair":
    senha = input("Digite sua senha: ")
    validar_senha(senha)

print(senhas)