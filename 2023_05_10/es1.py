# Scrivi un programma in Python per estrarre valori da un dizionario noto e crea una lista di liste da questi valori.

dizionario = [
    {"nome": "Alex", "cognome": "Rossi", "phone": "34333444"},
    {"nome": "Paolo", "cognome": "Rossi", "phone": "3433334"},
    {"nome": "Mario", "cognome": "Rossi", "phone": "34333344"},
]

[("nome", "Alex"), ("cognome")]

output = [
    ["Alex", "Rossi", "34333444"],
    # ...
]

output = []
for item in dizionario:
    output_item = []
    for k, v in item.items():
        output_item.append(v)
    # output_item = [v for k, v in item.items()]
    output.append(output_item)
    # output = [[v for k, v in item.items()] for item in dizionario]
