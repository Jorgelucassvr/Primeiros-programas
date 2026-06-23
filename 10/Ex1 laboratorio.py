



sensores = {}
with open ("/Users/jorgelucasvieira/Documents/Introdrucao a algoritmos/10/leitura.txt", "r") as arquivo:
    for linha in arquivo:
        codigo_sensor , Data , temperatura = linha.strip().split(";")
        try: float(temperatura)
        except ValueError:
            print("erro no sensor:",codigo_sensor)

        if temperatura != "erro":
            if codigo_sensor not in sensores:
                sensores[codigo_sensor] = {
                "quantidade": 0,
                "soma": 0.0,
                "menor temperatura": float(temperatura),
                "maior temperatura": float(temperatura),
                "media": 0.0
             }
            sensores[codigo_sensor]["quantidade"]+=1
            sensores[codigo_sensor]["soma"]+=float(temperatura)
            if sensores[codigo_sensor]["menor temperatura"] > float(temperatura):
                    sensores[codigo_sensor]["menor temperatura"] = float(temperatura)
            if sensores[codigo_sensor]["maior temperatura"] < float(temperatura):
                 sensores[codigo_sensor]["maior temperatura"] = float(temperatura)
for _ in sensores:
     sensores[_]["media"] = sensores[_]["soma"] / sensores[_]["quantidade"]
with open("relatorio_sensores.txt","w") as relatorio:
     for _ in sensores:
          nome = [_]
          quantidade = sensores[_]["quantidade"]
          soma = sensores[_]["soma"]
          menor_temperatura = sensores[_]["menor temperatura"]
          maior_temperatura = sensores[_]["maior temperatura"]
          media = sensores[_]["media"]
          linha_relatorio = (
          f"{nome}"
          " quantidade "f"{quantidade}; "
          "soma "f"{soma}; "
          "menor temperatura "f"{menor_temperatura}; "
          "maior_temperatura " f"{maior_temperatura}; "
          "media "f"{media}")
          relatorio.write(linha_relatorio + "\n")