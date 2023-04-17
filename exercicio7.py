with open("names.txt", "r", encoding="utf-8") as open_file:
    all_text = open_file.read()

nomes = all_text.split("\n")
ocorrencias = {}

for nome in nomes:
    if nome in ocorrencias:
        ocorrencias[nome] += 1
    else:
        ocorrencias[nome] = 1

for nome, ocorrencia in ocorrencias.items():
    print(f"{nome}: {ocorrencia} vezes")